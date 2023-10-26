import { createResource } from 'frappe-ui'
import { computed, reactive } from 'vue'
import router from '@/router'
import { session } from './session'

let usersByName = reactive({})
export let users = createResource({
  url: 'opssalesportal.api.auth.get_user_info',
  cache: 'Users',
  initialData: [],
  transform(users) {
    return users
  },
  onError(error) {
    if (error && error.exc_type === 'AuthenticationError') {
      router.push('/login')
    }
  },
})

export function getUser(email) {
  if (!email || email === 'sessionUser') {
    email = session.user
  }
  if (!usersByName[email]) {
    usersByName[email] = {
      name: email,
      email: email,
      full_name: email.split('@')[0],
      user_image: null,
      role: null,
    }
  }
  return usersByName[email]
}

export let activeUsers = computed(() => {
  return users.data.filter((user) => user.enabled)
})
