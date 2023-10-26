<template>
  <div class="project_page">
    <div class="xl:flex lg:block block xl:gap-[30px] gap-[15px]">
      <div class="google_map xl:w-6/12 lg:w-full w-full xl:sticky top-0">
        <GoogleMap api-key="AIzaSyDpPcBtSaGdqT9_Uuk9B5r84rXh2xGqh3M" class="h-[calc(100vh-99.55px)]" style="width: 100%;"
          :center="center" :zoom="10">
          <Marker v-for="infoWindow in infoWindowList" :options="{ position: infoWindow.position }"
            :key="infoWindow.project.name">
            <InfoWindow class="p-0" :visible="infoWindow.show">
              <ProjectCard class="max-w-[350px] w-full bg-white border border-gray-200 rounded-[10px]"
                :project="infoWindow.project" :infowindow="true" />
            </InfoWindow>
          </Marker>
        </GoogleMap>
        <!-- <GoogleMaps /> -->
      </div>
      <div
        class="overflow-y-hidden h-[calc(100vh-99.55px)] relative flex-auto listing_container xl:w-6/12 lg:w-full w-full py-[30px] pr-[20px] xl:pl-[0px] lg:pl-[20px] pl-[20px] ">
        <div class="total_res mb-[30px]">
          <div class="result text-heading">{{ total }} Search results</div>
        </div>
        <div v-show="loading" class="loader absolute inset-0">
          <div class="flex items-center justify-center h-full">
            <svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 24 24">
              <circle cx="18" cy="12" r="0" fill="currentColor">
                <animate attributeName="r" begin=".67" calcMode="spline" dur="1.5s"
                  keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0">
                </animate>
              </circle>
              <circle cx="12" cy="12" r="0" fill="currentColor">
                <animate attributeName="r" begin=".33" calcMode="spline" dur="1.5s"
                  keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0">
                </animate>
              </circle>
              <circle cx="6" cy="12" r="0" fill="currentColor">
                <animate attributeName="r" begin="0" calcMode="spline" dur="1.5s"
                  keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0">
                </animate>
              </circle>
            </svg>
            <b>Loading...</b>
          </div>
        </div>
        <div :class="{ 'opacity-50': loading == true }"
          class="grid xl:grid-cols-2 lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-4 justify-center h-[calc(100vh-99.55px)] overflow-y-scroll"
          id="scrollable-div" @scroll="handleScroll">
          <ProjectCard v-for="project in projectList" :key="project.name"
            class="w-full bg-white border border-gray-200 rounded-[10px]" :project="project" :infowindow="false" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Badge, Button, createResource } from 'frappe-ui'
import { defineComponent } from 'vue'
import { GoogleMap, Marker, InfoWindow } from 'vue3-google-map'
import ProjectCard from '../components/ProjectCard.vue'
import GoogleMaps from '../components/GoogleMap.vue'

export default defineComponent({
  name: 'Project',
  components: { GoogleMap, Marker, Badge, Button, InfoWindow, ProjectCard, GoogleMaps },
  data() {
    return {
      center: { lat: -25.093557, lng: 132.918085 },
      projectList: [],
      infoWindowList: [],
      total: 0,
      page: 1,
      loading: true,
      limit: 20
    }
  },
  methods: {
    getdata() {
      let filter = { available: 'no' }
      for (const key in this.$route.query) {
        if (
          this.$route.query.hasOwnProperty(key) &&
          this.$route.query[key] !== null &&
          this.$route.query[key] !== 'false' &&
          this.$route.query[key] !== '0' &&
          this.$route.query[key]
        ) {
          filter[key] = this.$route.query[key]
        }
      }
      this.loading = true; // Show the loader
      const data = createResource({
        method: 'post',
        url: 'opssalesportal.api.realestate_project.get_project_list',
        params: {
          filter,
          limit: this.limit,
          start_index: this.page == 1 ? 0 : this.limit * this.page,
        }
      })
      return data.reload()
    },
    async handleScroll() {
      const scrollableDiv = document.getElementById('scrollable-div')
      if (
        scrollableDiv.scrollTop + scrollableDiv.clientHeight >=
        scrollableDiv.scrollHeight
      ) {
        if (
          this.total / this.limit > 1 &&
          this.total / this.limit > this.page && !this.loading
        ) {
          this.page++
          const response = await this.getdata()
          setTimeout(() => {
            this.loading = false;
            this.projectList = [...this.projectList, ...response.projects]
            this.markerCreate()
          }, 1000);
        }
      }
    },
    markerCreate() {
      const infos = [];
      this.projectList.forEach((project, i) => {
        if (project?.coordinate) {
          let coordinate = JSON.parse(project.coordinate).features[0].geometry.coordinates;
          let marker = {
            project,
            name: project.name,
            show: true,
            position: {
              lat: coordinate[1],
              lng: coordinate[0]
            }
          };
          infos.push(marker);
        }
      })
      this.infoWindowList = infos
    }
  },
  async mounted() {
    const response = await this.getdata()
    setTimeout(() => {
      this.projectList = response.projects
      this.total = response.total
      this.loading = false;
      this.markerCreate()
    }, 1000);
    console.log(this.page);
    console.log(this.limit);
  }
})
</script>
