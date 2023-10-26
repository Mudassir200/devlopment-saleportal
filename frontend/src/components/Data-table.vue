<template>
  <div class="stages_table_comp">
    <div class="table_area w-full px-[30px]">
      <slot />
      <!-- Table -->
      <div class="flex flex-col mb-[20px]">
        <div class=" sm:-mx-6 lg:-mx-8">
          <div class="py-2 sm:px-6 lg:px-8">
            <div class="overflow-x-auto">
              <table class="text-center text-sm font-light w-full overflow-auto">
                <thead class="border-b bg-neutral-800 font-medium dark:border-neutral-500 dark:bg-neutral-900">
                  <tr>
                    <th v-for="(column, index) in tableColumns" :key="index" :colspan="column.colspan"
                      v-show="showColumnConditions(column)" class="px-4 py-4 font-normal whitespace-nowrap">
                      {{ column.title }}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(item, rowIndex) in paginatedData" :key="rowIndex" class="border-b dark:border-neutral-500">
                    <td v-for="(column, colIndex) in tableColumns" :key="colIndex"
                    v-show="showColumnConditions(column)" class="whitespace-nowrap px-4 py-4">
                      <span v-if="column.value === 'badge'"><span v-html="item[column.value]"></span></span>
                      <div class="flex gap-2" v-else-if="column.value === 'action'">
                        <button v-for="(action, actionIndex) in item[column.value]" :key="actionIndex"
                          @click="action.action()" :class="action.class" v-html="action.html" />
                      </div>
                      <span v-else-if="column.towcol && column.col && column.join">{{ [`$${item[column.col[0]] ||
                        0}`, `$${item[column.col[1]] || 0}`].join(" - ") }}</span>
                      <span v-else-if="column?.price && column?.price">{{ withPrice(item[column.value]) }}</span>
                      <span v-else>{{ item[column.value] }}</span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      <!-- pagination -->
      <div class="flex justify-between items-center flex-wrap gap-[20px]">
        <div>{{ entriesRange }}</div>
        <div class="flex gap-[5px]">
          <button @click="previousPage" :disabled="currentPage === 1"
            class="md:py-[10px] py-[5px] md:px-[16px] px-[10px] bg-white rounded-[5px]">Previous</button>
          <div v-for="page in Math.ceil(tableData.length / pageSize)" :key="page">
            <button @click="changePage(page)" :disabled="currentPage === page"
              :class="{ 'bg-primary text-white': isActivePage(page), 'bg-white': !isActivePage(page) }"
              class="md:py-[10px] py-[5px] md:px-[16px] px-[10px] rounded-[5px]">{{ page }}</button>
          </div>
          <button @click="nextPage" :disabled="currentPage === Math.ceil(tableData.length / pageSize)"
            class="md:py-[10px] py-[5px] md:px-[16px] px-[10px] bg-white rounded-[5px]">Next</button>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>

import { Button } from 'frappe-ui'
export default {
  name: 'DataTable',
  components: {
    Button
  },
  data() {
    return {
      currentPage: 1, // Current page number
      pageSize: 10, // Number of items per page
      sortColumn: '', // Column to sort by (initially empty)
      sortDirection: 'asc', // Sort direction ('asc' or 'desc')
      value: null
    };
  },
  computed: {
    paginatedData() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.tableData.slice(startIndex, endIndex);
    },
    entriesRange() {
      const from = (this.currentPage - 1) * this.pageSize + 1;
      const to = Math.min(this.currentPage * this.pageSize, this.tableData.length);
      const totalEntries = this.tableData.length;
      return `Showing ${from} to ${to} of ${totalEntries} entries`;
    },
  },
  methods: {
    showColumnConditions: function (column) {
      if (column?.multistage == true) {
        if (this.project_detail.multistage) return true;
        else return false;
      }
      if (column?.multistage_conType == true) {
        if (this.project_detail.multistage || (!this.project_detail.multistage && this.project_detail.contract_type == "Two Part")) return true;
        else return false;
      }
      return true;
    },
    withPrice: function (val) {
      return val !== undefined && val !== null ? `$${val}` : `$0`;
    },
    changePage(page) {
      this.currentPage = page;
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < Math.ceil(this.tableData.length / this.pageSize)) {
        this.currentPage++;
      }
    },
    isActivePage(page) {
      return this.currentPage === page;
    },
    toggleOptions() {
      this.showOptions = !this.showOptions;
    },
    toggleOption(option) {
      if (this.selectedOptions.includes(option)) {
        this.selectedOptions = this.selectedOptions.filter((item) => item !== option);
      } else {
        this.selectedOptions.push(option);
      }
    },
  },
  props: {
    project_detail: Object,
    tableData: Array, // An array of objects representing table rows
    tableColumns: Array, // An array of objects representing table columns
    perpageData: Number
  },
}
</script>
<style src="@vueform/multiselect/themes/default.css"></style>
  