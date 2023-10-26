<template>
  <div class="home">
    <section class="section p-5">
      <div class="form">
          <div class="grid lg:grid-cols-4 md:grid-cols-2 grid-cols-1 gap-4 mb-7">
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Project:" :options="projects"
                v-model="filter.project" size="lg" variant="outline" />
            </div>
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="State:" :options="states" v-model="filter.state"
                size="lg" variant="outline" />
            </div>
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Agent:" :options="agents" v-model="filter.agent"
                size="lg" variant="outline" />
            </div>
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Contract Type:" :options="contract_type"
                v-model="filter.contract_type" size="lg" variant="outline" />
            </div>
          </div>
          <div class="grid lg:grid-cols-4 md:grid-cols-2 grid-cols-1 gap-4 mb-7">
            <div class="field">
              <FormControl type="number" size="lg" variant="outline" placeholder="0.00" :min="min" :max="max" step="10000"
                :label="'Min. Price: (' + min + ')'" v-model="filter.min" />
            </div>
            <div class="field">
              <FormControl type="number" size="lg" variant="outline" placeholder="0.00" :min="min" :max="max" step="10000"
                :label="'Max. Price: (' + max + ')'" v-model="filter.max" />
            </div>
            <div class="field">
              <FormControl type="date" size="lg" variant="outline" placeholder="Select Date" label="Settlement From:"
                v-model="filter.from" />
            </div>
            <div class="field">
              <FormControl type="date" size="lg" variant="outline" placeholder="Select Date" label="Settlement To:"
                v-model="filter.to" />
            </div>
          </div>
          <div class="grid lg:grid-cols-4 md:grid-cols-2 grid-cols-1 gap-4 mb-7">
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Dwellings Type:" :options="property_type"
                v-model="filter.property_type" size="lg" variant="outline" />
            </div>
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Bedrooms:" :options="bedroom"
                v-model="filter.bedroom" size="lg" variant="outline" />
            </div>
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Bathrooms:" :options="bathroom"
                v-model="filter.bathroom" size="lg" variant="outline" />
            </div>
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Carparks:" :options="carparks"
                v-model="filter.carpark" size="lg" variant="outline" />
            </div>
          </div>
          <div class="grid lg:grid-cols-4 md:grid-cols-2 grid-cols-1 gap-4 mb-7">
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Constr. Started:" :options="constr_started"
                v-model="filter.constr_started" size="lg" variant="outline" />
            </div>
            <div class="field">
              <FormControl type="number" size="lg" variant="outline" placeholder="0" min="0" max="20"
                label="Min. Yield %:" v-model="filter.min_yield" />
            </div>
            <div class="field">
              <FormControl type="select" placeholder="Placeholder" label="Search By:" :options="Search_By"
                v-model="filter.realestate_type" size="lg" variant="outline" />
            </div>
            <div class="field flex flex-col justify-center gap-2">
              <FormControl type="checkbox" label="Titled or within 90 days" v-model="filter.titlewithin" size="lg" />
              <FormControl type="checkbox" label="Available Only" v-model="filter.available" size="lg" />
            </div>
          </div>
          <div class="buttons flex gap-4">
            <Button variant="solid" size="lg" label="Search Property" theme="primary"
              class="bg-primary text-white px-[30px]" v-on:click.prevent="redirectList" />
            <Button variant="solid" size="lg" label="Reset Filter" theme="secondary"
              class="bg-secondary text-heading px-[30px]" v-on:click.prevent="resetFilters" />
          </div>
      </div>
    </section>
  </div>
</template>
<script>
import { FormControl, Button, createResource, Select } from 'frappe-ui'
import homefilter from '../data/filter.json'
export default {
  name: 'Home',
  components: {
    FormControl,
    Button,
    Select,
  },
  data() {
    return {
      projects: [],
      property_type: [],
      agents: [],
      states: [],
      min: 0,
      max: 0,
      filter: {
        project: '',
        property_type: '',
        contract_type: '',
        agent: '',
        state: '',
        min: '',
        max: '',
        from: '',
        to: '',
        bathroom: '',
        bedroom: '',
        carpark: '',
        constr_started: '',
        available: false,
        min_yield: '',
        realestate_type: '',
        titlewithin: false,
      },
      contract_type: homefilter.contract_type,
      bathroom: homefilter.bedroom,
      bedroom: homefilter.bedroom,
      carparks: homefilter.carparks,
      constr_started: homefilter.constr_started,
      Search_By: homefilter.search_by,
    }
  },
  methods: {
    getdata() {
      const data = createResource({
        method: 'Get',
        url: 'opssalesportal.api.realestate_project.get_home_filter',
      })
      return data.reload()
    },
    redirectList() {
      this.$router.push({
        name: 'Project',
        query: { ...this.filter },
      })
    },
    resetFilters() {
      for (let key in this.filter) {
          if (this.filter.hasOwnProperty(key)) {
              this.filter[key] = null;
          }
      }
    },
  },
  async mounted() {
    const response = await this.getdata()
    this.projects = [
      { label: 'Select Project', value: '' },
      ...response.projects,
    ]
    this.property_type = [
      { label: 'Select Property Type', value: '' },
      ...response.propertyTypes.map((item) => {
        return {
          value: item,
          label: item,
        }
      }),
    ]
    this.states = [
      { label: 'Select State', value: '' },
      ...response.states.map((item) => {
        return {
          value: item,
          label: item,
        }
      }),
    ]
    this.agents = [
      { label: 'Select Agent', value: '' },
      ...response.agents.map((item) => {
        return {
          value: item.name,
          label: item.vendor_name,
        }
      }),
    ]
    this.min = response.min
    this.max = response.max
  },
}
</script>
