import requests
from dateutil import parser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.db import models

from .models import OPProject, WorkPackage, OPUser, OPStatus
from .serializers import ProjectSerializer

OPENPROJECT_URL = "https://community.openproject.org/api/v3"

class PingView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        return Response({"message": "pong"})

class OpenProjectStatusView(APIView):
    def get(self, request):
        try:
            resp = requests.get(f"{OPENPROJECT_URL}/projects", timeout=5)
            status_code = resp.status_code
        except requests.RequestException:
            status_code = "error"
        return Response({"openproject_status": status_code})

class SyncView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        self.sync_projects()
        self.sync_statuses()
        self.sync_users()
        self.sync_work_packages()
        return Response({"detail": "synchronized"})

    def fetch_collection(self, endpoint):
        resp = requests.get(f"{OPENPROJECT_URL}/{endpoint}?pageSize=100")
        resp.raise_for_status()
        return resp.json().get("_embedded", {}).get("elements", [])

    def sync_projects(self):
        for proj in self.fetch_collection("projects"):
            OPProject.objects.update_or_create(
                openproject_id=proj["id"],
                defaults={"name": proj["name"], "identifier": proj["identifier"]},
            )

    def sync_statuses(self):
        for st in self.fetch_collection("statuses"):
            OPStatus.objects.update_or_create(
                openproject_id=st["id"], defaults={"name": st["name"]}
            )

    def sync_users(self):
        for user in self.fetch_collection("users"):
            OPUser.objects.update_or_create(
                openproject_id=user["id"], defaults={"name": user["name"]}
            )

    def sync_work_packages(self):
        for wp in self.fetch_collection("work_packages"):
            project_id = int(wp["_links"]["project"]["href"].split("/")[-1])
            project = OPProject.objects.filter(openproject_id=project_id).first()
            status_id = int(wp["_links"]["status"]["href"].split("/")[-1])
            status = OPStatus.objects.filter(openproject_id=status_id).first()
            assignee = None
            if wp["_links"].get("assignee"):
                assignee_id = int(wp["_links"]["assignee"]["href"].split("/")[-1])
                assignee = OPUser.objects.filter(openproject_id=assignee_id).first()
            updated = parser.isoparse(wp["updatedAt"])
            WorkPackage.objects.update_or_create(
                openproject_id=wp["id"],
                defaults={
                    "subject": wp["subject"],
                    "project": project,
                    "status": status,
                    "assignee": assignee,
                    "updated_at": updated,
                },
            )

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OPProject.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        # annotate with KPI data
        qs = qs.annotate(
            open_packages=models.Count(
                "workpackage",
                filter=models.Q(workpackage__status__name__iexact="open"),
            ),
            closed_packages=models.Count(
                "workpackage",
                filter=models.Q(workpackage__status__name__iexact="closed"),
            ),
        )
        return qs
