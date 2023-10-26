<template>
    <div id="stages" v-if="project_detail?.multistage"
        class="stages_table-container max-w-[1780px] m-auto py-[30px] rounded-[10px] mb-[30px]">
        <div class="table_heading text-[22px] font-medium mb-[20px] pl-[30px]">Stages of Orbis Projects</div>
        <DataTable :tableData="stagestableData" :tableColumns="stagestableColumns" :project_detail="project_detail" />
    </div>
</template>
<script>
import { createResource } from 'frappe-ui'
import DataTable from '../Data-table.vue'
import projectdetail from '../../data/projectdetails.json';
export default {
    name: 'StageList',
    components: {
        DataTable,
    },
    props: {
        project_detail: Object
    },
    data() {
        return {
            stagestableColumns: projectdetail.stagestableColumns,
            stagestableData: [],
        }
    },
    methods: {
        getstagedata() {
            const data = createResource({
                method: 'Get',
                url: `opssalesportal.api.realestate_project.get_stage_project?project=${this.$route.params.id}`
            })
            return data.reload()
        }
    },
    async mounted() {
        const result = await this.getstagedata();
        this.stagestableData = await result.map((item) => {
            let stageitem = { ...item };
            if (item.multistage == 0) {
                if(item.holding_deposit > 0){
                    if(item.deposit_type === "Fixed")
                        stageitem = {...stageitem, holding_deposit:`$${item.holding_deposit}`}
                    else
                        stageitem = {...stageitem, holding_deposit:`${item.holding_deposit}%`}
                }else{
                    stageitem = {...stageitem, holding_deposit:"TBA"}
                }
            }else{
                stageitem = {...stageitem, holding_deposit:null}
            }
            stageitem.action = [
                {
                    class: "bg-secondary rounded-[5px] text-heading py-[7px] px-[12px] ",
                    html: '<div class="flex items-center gap-1"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8" fill="none"><path d="M11.9275 3.69584C10.7977 1.49146 8.56105 0 6 0C3.43895 0 1.20166 1.4925 0.0724887 3.69605C0.0248307 3.79032 0 3.89448 0 4.00011C0 4.10575 0.0248307 4.2099 0.0724887 4.30417C1.20228 6.50855 3.43895 8.00002 6 8.00002C8.56105 8.00002 10.7983 6.50751 11.9275 4.30397C11.9752 4.20969 12 4.10554 12 3.9999C12 3.89427 11.9752 3.79011 11.9275 3.69584ZM6 7.00001C5.40665 7.00001 4.82663 6.82407 4.33329 6.49442C3.83994 6.16478 3.45542 5.69624 3.22836 5.14806C3.00129 4.59988 2.94188 3.99668 3.05764 3.41474C3.17339 2.83279 3.45912 2.29824 3.87868 1.87868C4.29823 1.45912 4.83278 1.1734 5.41473 1.05765C5.99667 0.94189 6.59987 1.0013 7.14805 1.22836C7.69623 1.45543 8.16477 1.83995 8.49441 2.33329C8.82406 2.82664 9.00001 3.40666 9.00001 4.00001C9.0002 4.39403 8.92273 4.78422 8.77203 5.14829C8.62134 5.51235 8.40037 5.84315 8.12175 6.12176C7.84314 6.40037 7.51234 6.62135 7.14828 6.77204C6.78422 6.92274 6.39402 7.00021 6 7.00001ZM6 2C5.82149 2.0025 5.64412 2.02906 5.47271 2.07896C5.614 2.27098 5.68181 2.50727 5.66382 2.74499C5.64584 2.98271 5.54326 3.20612 5.37469 3.37469C5.20611 3.54327 4.98271 3.64585 4.74499 3.66383C4.50727 3.68182 4.27097 3.61401 4.07895 3.47271C3.96961 3.87555 3.98935 4.30252 4.13539 4.69355C4.28143 5.08458 4.54641 5.41996 4.89304 5.6525C5.23967 5.88504 5.6505 6.00302 6.0677 5.98984C6.4849 5.97667 6.88746 5.83299 7.21873 5.57903C7.54999 5.32508 7.79328 4.97364 7.91434 4.57417C8.03541 4.17471 8.02816 3.74734 7.89361 3.35221C7.75906 2.95708 7.50399 2.6141 7.1643 2.37153C6.82461 2.12896 6.41741 1.99902 6 2Z" fill="#596263"/></svg> View </div>',
                    action: () => {
                        this.$router.push({ name: "StageDetail", params: { id: item.name } });
                    }
                },
                {
                    class: "bg-primary rounded-[5px] text-white py-[7px] px-[12px]",
                    html: "Master Plan",
                }
            ]
            return stageitem
        })
    }
}
</script>