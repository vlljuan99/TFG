<template>
  <div>
    <div v-if="!token">
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      <button @click="login">Login</button>
    </div>
    <div v-else>
      <button @click="fetchStatus">Check OpenProject</button>
      <p v-if="status">Status: {{ status }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
export default {
  setup() {
    const username = ref('')
    const password = ref('')
    const token = ref(localStorage.getItem('token') || '')
    const status = ref('')

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

    return { username, password, token, login, fetchStatus, status }
  }
}
</script>
