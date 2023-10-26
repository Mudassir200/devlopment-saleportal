import { computed, reactive } from 'vue'
import { createResource } from 'frappe-ui'
import router from '@/router'

export function sessionUser() {
  let cookies = new URLSearchParams(document.cookie.split('; ').join('&'))
  let _sessionUser = cookies.get('user_id')
  if (_sessionUser === 'Guest') {
    _sessionUser = null
  }
  return _sessionUser
}

export function user_info() {
  return createResource({
    url: 'opssalesportal.api.auth.get_user_info',
    onSuccess(user) {
      return user
    },
  })
}

export let session = reactive({
  login: createResource({
    url: 'opssalesportal.api.auth.login',
    makeParams({ email, password }) {
      return {
        usr: email,
        pwd: password,
      }
    },
    onSuccess(data) {
      session.userInfo.reload()
      session.user = sessionUser()
      session.login.reset()
      const route = data.default_route || '/';
      router.replace({ path: route })

    },
  }),
  logout: createResource({
    url: 'logout',
    onSuccess() {
      session.user = sessionUser()
      router.replace({ name: 'Login' })
    },
  }),
  user: sessionUser(),
  userInfo: user_info(),
  isLoggedIn: computed(() => !!session.user),
})
