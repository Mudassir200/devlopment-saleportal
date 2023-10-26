<template>
  <div class="property_detail">
    <div class="banner-section">
      <div class="property_images-container grid lg:grid-cols-2 md:grid-cols-1 grid-cols-1 gap-[10px]">
        <div class="featured_image relative">
          <div class="prices flex flex-wrap gap-x-[25px] gap-y-[5px] items-center absolute sm:bottom-[25px] bottom-[15px] sm:left-[25px] left-[15px] z-10">
            <div class="property_price lg:text-[34px] sm:text-[25px] text-[20px] font-bold text-white">
              Price: ${{ property_detail.total_price }}
            </div>
            <div class="land_price font-medium lg:text-[20px] text-[15px] text-white">
              Land: ${{property_detail.land_price}}
            </div>
            <div class="build_price font-medium lg:text-[20px] text-[15px] text-white">
              Build: ${{property_detail.build_price}}
            </div>
          </div>
          <a :href="'/src/assets/images/login_bg.png'" :data-fancybox="'gallery'" class="relative">
            <img :src="featured_image" alt="featured_image" class="h-full object-cover w-full" />
            <div class="overlay absolute bottom-0 inset-x-0 top-1/2 bg-gradient-to-t from-[#000]"></div>
          </a>
        </div>
        <div class="property_images grid grid-cols-2 gap-[10px]">
          <div v-for="(item, index) in images" :key="index" v-show="index < 4"
            class="property_image relative max-h-[344.09px]">
            <div v-if="item.index == 3" class="overlay absolute inset-0 bg-[#000] opacity-50"></div>
            <div v-if="item.index == 3" class="overlay absolute top-1/2 left-1/2 text-white translate-x-[-50%]">
              <a :href="'/src/assets/images/login_bg.png'" :data-fancybox="'gallery'">View All Images</a>
            </div>
              <img :src="item.image" alt="" class="w-full object-cover h-full" />
              {{ index.length }}
          </div>
        </div>
      </div>
    </div>
    <div class="grid xl:grid-cols-4 lg:grid-cols-4 md:grid-cols-1 grid-cols-1 xl:px-10 lg:px-5 px-5 py-7 gap-6">
      <div class="lg:col-span-3 md:col-span-1 col-span-1">
        <div>
          <div class="detail_section mb-[30px]">
            <Propertydetails :property_detail="property_detail" :project_detail="project_detail" />
          </div>
          <div v-if="project_detail?.project_documents && project_detail.project_documents.length > 0" class="document-section mb-[30px] px-[20px]">
            <Documents :project_detail="project_detail" />
          </div>
          <Location :project_detail="project_detail" :project_location="project_location" />
        </div>
      </div>
      <div class="sidebar">
       <Sidebar :project_detail="project_detail" />
      </div>
    </div>
  </div>
</template>


<script>
import "@fancyapps/fancybox/dist/jquery.fancybox.min.css" // Import Fancybox CSS
import "@fancyapps/fancybox/dist/jquery.fancybox.min.js" // Import Fancybox JS
import Propertydetails from "../components/Property/Detail.vue"
import Documents from '../components/Documents.vue'
import Location from '../components/Location.vue'
import Sidebar from "../components/Property/sidebar.vue"
import { createResource } from 'frappe-ui'
export default {
  name: 'PropertyDetail',
  components: {
    Propertydetails,
    Sidebar,
    Documents,
    Location
  },
  data(){
    return{
      images: [],
      featured_image: '',
      property_detail: {},
      project_detail: {},
      project_location: { lat: 40.689247, lng: -74.044502 },
    }
  },
  mounted() {
    this.initializeFancybox();
  },
  methods: {
    getdata() {
      const data = createResource({
        method: 'Get',
        url: `opssalesportal.api.property.get_property_details?property=${this.$route.params.id}`
      })
      console.log(data);
      return data.reload()
    },
    initializeFancybox() {
      const galleryImages = document.querySelectorAll("[data-fancybox^='gallery']");
      $(galleryImages).fancybox({
        type: "image",
        spinnerTpl: false, // Disable the loading spinner
      });
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
    this.property_detail = response.propertydetails
    this.project_detail = response.projectdetails
    this.featured_image = this.property_detail.property_featured_image
    this.images = [ ...this.project_detail.project_images]
    if (this.project_detail?.coordinate) {
      let coordinate = JSON.parse(this.project_detail.coordinate).features[0].geometry.coordinates;
      this.project_location = {
        lat: coordinate[1],
        lng: coordinate[0]
      }
    }
  }
}
</script>