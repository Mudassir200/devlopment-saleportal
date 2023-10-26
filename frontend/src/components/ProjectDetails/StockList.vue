<template>
    <div id="property_Stock" class="pr_stock_table-container">
        <div class="table_heading text-[22px] font-medium mb-[20px] pl-[30px]">Property stock of Orbis Projects</div>
        <DataTable :tableData="stocktableData" :tableColumns="stocktableColumns" :project_detail="project_detail">
            <!-- table filter -->
            <div class="table_filter mb-[20px]">
                <form>
                    <div class="filter-fields flex flex-wrap items-end gap-x-[10px] gap-y-[20px]">
                        <FormControl v-if="project_detail.multistage == 1" type="select" label="Stages" :options="stages"
                            v-model="filter.stage" size="md" variant="outline" class="flex-auto" />
                        <FormControl v-if="project_detail.multistage == 1" type="date" size="md" variant="outline"
                            placeholder="Select Date" label="Settlement From" v-model="filter.from" class="flex-auto" />
                        <FormControl v-if="project_detail.multistage == 1" type="date" size="md" variant="outline"
                            placeholder="Select Date" label="Settlement To" v-model="filter.from" class="flex-auto" />
                        <FormControl v-if="project_detail.multistage == 1" type="checkbox" label="Titled or within 90 days"
                            v-model="filter.titlewithin" size="md" />
                        <FormControl type="select" label="Bedrooms" :options="bedroom" v-model="filter.bedroom" size="md"
                            variant="outline" class="flex-auto" />
                        <FormControl type="select" label="Bathrooms" :options="bathroom" v-model="filter.bathroom" size="md"
                            variant="outline" class="flex-auto" />
                        <FormControl type="select" label="Contract Type" :options="contract_type"
                            v-model="filter.contract_type" size="md" variant="outline" class="flex-auto" />
                        <FormControl type="number" size="md" variant="outline" placeholder="0.00" :min="min" :max="max"
                            step="10000" :label="'Min. Price: (' + minPrice + ')'" v-model="filter.min" class="flex-auto" />
                        <FormControl type="number" size="md" variant="outline" placeholder="0.00" :min="min" :max="max"
                            step="10000" :label="'Max. Price: (' + maxPrice + ')'" v-model="filter.max" class="flex-auto" />
                        <div class="flex-auto max-w-[130px] w-full">
                            <label class="block text-base text-gray-600" for="frappe-ui-6">Status</label>
                            <Multiselect v-model="filter.property_status" :options="property_status" mode="multiple" :noOptionsText="true"
                                :hideSelected="false" :close-on-select="false" :searchable="true">
                                <template v-slot:multiplelabel="{ values }">
                                    <div class="multiselect-multiple-label flex-col overflow-hidden pt-[4px]">
                                        <div v-for="(item, index) in values" :key="index">
                                            {{ item.value }}
                                        </div>
                                    </div>
                                </template>
                            </Multiselect>
                        </div>
                        <Button variant="solid" size="md" label="Filter" theme="secondary"
                            class="bg-secondary text-heading px-[17px]" v-on:click.prevent="getpropertiesdata" />
                        <input type="reset" value="Reset"
                            class="bg-primary text-white px-[15px] py-[4px] rounded-md cursor-pointer">
                        <FormControl :type="'search'" v-model="query" size="md" variant="outline" placeholder="Search.." />
                    </div>
                </form>
            </div>
        </DataTable>
    </div>
</template>
<script>
import { createResource } from 'frappe-ui'
import DataTable from '../Data-table.vue'
import projectdetail from '../../data/projectdetails.json';
import filter from '../../data/filter.json'
import { FormControl, Button } from 'frappe-ui'
import Multiselect from '@vueform/multiselect'

export default {
    name: 'StockList',
    components: {
        DataTable,
        Button,
        FormControl,
        Multiselect
    },
    props: {
        project_detail: Object
    },
    data() {
        return {
            query: "",
            filter: {
                project: '',
                property_type: '',
                contract_type: '',
                agent: '',
                status: '',
                min: "",
                max: "",
                from: "",
                to: "",
                bathroom: '',
                bedroom: '',
                carpark: '',
                available: false,
                min_yield: "",
                realestate_type: '',
                titlewithin: false,
                stage: "",
                property_status: [],
            },
            minPrice: 0,
            maxPrice: 0,
            stages: [],
            contract_type: filter.contract_type,
            property_status: [],
            bathroom: filter.bedroom,
            bedroom: filter.bedroom,
            stocktableColumns: projectdetail.stocktableColumns,
            stocktableData: [],
        }
    },
    methods: {
        async getpropertiesdata() {
            let filter = {}
            for (const key in this.filter) {
                if (
                    this.filter.hasOwnProperty(key) &&
                    this.filter[key] !== null &&
                    this.filter[key] !== 'false' &&
                    this.filter[key] !== '0' &&
                    this.filter[key]
                ) {
                    filter[key] = this.filter[key]
                }
            }
            const data = createResource({
                method: 'POST',
                url: `opssalesportal.api.realestate_project.get_project_properties`,
                params: {
                    project: this.$route.params.id,
                    filter
                }
            })
            const getpropertiesdata = await data.reload();
            this.stocktableData = await getpropertiesdata.properties.map((item) => {
                let stockitem = { ...item };
                stockitem.action = [
                    {
                        class: "bg-secondary rounded-[5px] text-heading py-[7px] px-[12px] ",
                        html: '<div class="flex items-center gap-1"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8" fill="none"><path d="M11.9275 3.69584C10.7977 1.49146 8.56105 0 6 0C3.43895 0 1.20166 1.4925 0.0724887 3.69605C0.0248307 3.79032 0 3.89448 0 4.00011C0 4.10575 0.0248307 4.2099 0.0724887 4.30417C1.20228 6.50855 3.43895 8.00002 6 8.00002C8.56105 8.00002 10.7983 6.50751 11.9275 4.30397C11.9752 4.20969 12 4.10554 12 3.9999C12 3.89427 11.9752 3.79011 11.9275 3.69584ZM6 7.00001C5.40665 7.00001 4.82663 6.82407 4.33329 6.49442C3.83994 6.16478 3.45542 5.69624 3.22836 5.14806C3.00129 4.59988 2.94188 3.99668 3.05764 3.41474C3.17339 2.83279 3.45912 2.29824 3.87868 1.87868C4.29823 1.45912 4.83278 1.1734 5.41473 1.05765C5.99667 0.94189 6.59987 1.0013 7.14805 1.22836C7.69623 1.45543 8.16477 1.83995 8.49441 2.33329C8.82406 2.82664 9.00001 3.40666 9.00001 4.00001C9.0002 4.39403 8.92273 4.78422 8.77203 5.14829C8.62134 5.51235 8.40037 5.84315 8.12175 6.12176C7.84314 6.40037 7.51234 6.62135 7.14828 6.77204C6.78422 6.92274 6.39402 7.00021 6 7.00001ZM6 2C5.82149 2.0025 5.64412 2.02906 5.47271 2.07896C5.614 2.27098 5.68181 2.50727 5.66382 2.74499C5.64584 2.98271 5.54326 3.20612 5.37469 3.37469C5.20611 3.54327 4.98271 3.64585 4.74499 3.66383C4.50727 3.68182 4.27097 3.61401 4.07895 3.47271C3.96961 3.87555 3.98935 4.30252 4.13539 4.69355C4.28143 5.08458 4.54641 5.41996 4.89304 5.6525C5.23967 5.88504 5.6505 6.00302 6.0677 5.98984C6.4849 5.97667 6.88746 5.83299 7.21873 5.57903C7.54999 5.32508 7.79328 4.97364 7.91434 4.57417C8.03541 4.17471 8.02816 3.74734 7.89361 3.35221C7.75906 2.95708 7.50399 2.6141 7.1643 2.37153C6.82461 2.12896 6.41741 1.99902 6 2Z" fill="#596263"/></svg> View </div>',
                        action: () => {
                            this.$router.push({ name: "PropertyDetail", params: { id: item.name } });
                        }
                    },
                    {
                        class: "bg-primary rounded-[5px] text-white py-[7px] px-[12px]",
                        html: "Master Plan",
                    }
                ]
                return stockitem

            })
            console.log(this.query);
        },

        get_properties_filter() {
            const data = createResource({
                method: 'Get',
                url: `opssalesportal.api.realestate_project.get_properties_filter?project=${this.$route.params.id}`
            })
            return data.reload()
        },
    },
    async mounted() {
        await this.getpropertiesdata();
        const getpropertiesfilter = await this.get_properties_filter();

        this.minPrice = getpropertiesfilter.min;
        this.maxPrice = getpropertiesfilter.max;
        this.property_status = getpropertiesfilter.property_status;
        this.stages = [
            { label: 'Select Stage', value: '' },
            ...getpropertiesfilter.stages.map((item) => {
                return {
                    value: item,
                    label: item,
                }
            }),
        ]
    }
}
</script>