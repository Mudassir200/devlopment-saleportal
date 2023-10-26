<template>
  <router-view v-if="['Onboarding', 'Login'].includes($route.name)" />
  <BaseLayout v-else-if="session.isLoggedIn">
    <router-view />
  </BaseLayout>
</template>
<script setup>
import { defineAsyncComponent } from 'vue'
import { session } from './data/session'

const BaseLayout = defineAsyncComponent(() =>
  import('../src/layout/base.vue')
)
</script>
