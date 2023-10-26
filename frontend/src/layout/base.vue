<template>
    <div>
        <HeaderNavigation/>
        <slot />
    </div>
</template>
<script>
import HeaderNavigation from '../layout/header.vue'

export default {
    name: 'BaseLayout',
    components: {
        HeaderNavigation
    },
}
</script>