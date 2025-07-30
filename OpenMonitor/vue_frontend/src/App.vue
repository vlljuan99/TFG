<template>
  <div>
    <div v-if="!token">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button @click="login">Login</button>
    </div>
    <div v-else>
      <div>
        <button @click="fetchStatus">Check OpenProject</button>
        <button @click="fetchProjects">Load KPIs</button>
      </div>
      <p v-if="status">Status: {{ status }}</p>
      <table v-if="projects.length">
        <thead>
          <tr>
            <th>Project</th>
            <th>Open</th>
            <th>Closed</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="p in projects" :key="p.openproject_id">
            <td>{{ p.name }}</td>
            <td>{{ p.open_packages }}</td>
            <td>{{ p.closed_packages }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue'
export default {
  setup() {
    const username = ref('')
    const password = ref('')
    const token = ref(localStorage.getItem('token') || '')
    const status = ref('')
    const projects = ref([])
    let interval

    const login = async () => {
      const res = await fetch('/openmonitor-api/token-auth/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username.value, password: password.value })
      })
      const data = await res.json()
      token.value = data.token
      localStorage.setItem('token', token.value)
    }

    const fetchStatus = async () => {
      const res = await fetch('/openmonitor-api/openproject/', {
        headers: { Authorization: `Token ${token.value}` }
      })
      const data = await res.json()
      status.value = data.openproject_status
    }

    const fetchProjects = async () => {
      const res = await fetch('/openmonitor-api/projects/', {
        headers: { Authorization: `Token ${token.value}` }
      })
      projects.value = await res.json()
    }

    const startPolling = () => {
      if (interval) clearInterval(interval)
      interval = setInterval(fetchProjects, 60000)
    }

    if (token.value) {
      fetchProjects()
      startPolling()
    }

    watch(token, (val) => {
      if (val) {
        fetchProjects()
        startPolling()
      } else if (interval) {
        clearInterval(interval)
      }
    })

    return { username, password, token, login, fetchStatus, fetchProjects, status, projects }
  }
}
</script>
