FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
# RUN npm install
RUN npm install && npx vite --version
COPY . .
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
