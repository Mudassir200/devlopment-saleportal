<template>
    <div class="bg-white rounded xl:p-[30px] lg:p-[20px] p-[20px] border">
        <p class="md:pb-[30px] pb-[20px] text-[16px] font-semibold text-gray-800">PROJECT DETAIL</p>
        <div class="w-full">
            <div class="xl:flex lg:block block xl:text-left lg:text-center text-center gap-[15px] items-center">
                <img :src="project_detail.featured_image" class="rounded-full xl:mb-0 lg:mb-3 mb-3 inline-block w-full h-full min-h-[100px] max-w-[100px]">
                <div class="agent_detail">
                    <h3 class="text-neutral-800 font-semibold mb-1">{{ project_detail.project_name }}</h3>
                    <div class="text-gray-600 text-sm leading-6 mb-2">{{ project_detail.full_address }}</div>
                    <button variant="solid" theme="primary" size="lg" class="text-primary font-medium text-base">
                        <router-link :to="'/project_detail/' + project_detail.name">View Project</router-link>
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { Button } from 'frappe-ui'
export default {
    name: 'Sidebar',
    components: {
        Button,
    },
    props:{
        project_detail: Object,
    }
}
</script>