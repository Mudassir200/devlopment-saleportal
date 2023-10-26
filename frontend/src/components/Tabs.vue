<template>
    <div class="tab_comp shadow-[0px_10px_50px_-10px_rgba(37,48,49,0.12)] overflow-auto">
      <div class="tab_items flex justify-center m-auto">
      <div v-for="(tab, index) in Tabs" :key="index" :class="[{ 'active': index === activeTab }]" @click="setActiveTab(index)" class="tab_item whitespace-nowrap px-[40px] py-[20px] border-white border-b-2 cursor-pointer" >
          <a :href="'#'+tab.id">{{tab.tab_item}}</a>
      </div>
      </div>
    </div>
  </template>
  <script>
  export default {
      name: 'tabs',
      props: {
          Tabs: Array,
      },
      data() {
            return {
            activeTab: 0
            }
        },
        methods: {
            setActiveTab(index) {
            this.activeTab = index;
            },
        },
  }
  </script>
  <style>
  .active {
    color: #84754E; /* Define your active tab styling here */
    border-color: #84754E;
    /* Add any other styles you want for the active tab */
  }
  </style>