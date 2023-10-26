<template>
    <div class="stage-detail">
        <div id="detail" >
          <Images :featuredImage="featured_image" :images="images"/>
            <div class="mb-[30px] sm:pt-[50px] pt-[30px] xl:px-[70px] lg:px-[50px] sm:px-[30px] px-[20px] gap-[40px]">
            <div class="project-details_section flex-auto">
              <Details :project_detail="project_detail" :projectSummury="projectSummury" />
            </div>
          </div>
        </div>
        <div v-show="showTabs" class="detail_tabs mb-[30px] fixed w-full top-0 bg-white z-50">
          <Tabs :Tabs="tabs"/>
        </div>
        <div class="stock_list bg-[#F6F7F8] max-w-[1780px] m-auto py-[30px] rounded-[10px]  mb-[30px]">
          <StockList :project_detail="project_detail" />
        </div>
        <div id="documents" class="document-section mb-[30px] px-[20px]">
          <Documents :project_detail="project_detail" />
        </div>
        <div id="locations" class="location-section mb-[30px] px-[20px]">
          <Location :project_detail="project_detail" :project_location="project_location" />
        </div>
        <div id="description" class="about-section max-w-[1780px] mx-auto mb-[30px] px-[20px]">
            <div class="description">
              <h5 class="discription_title font-medium text-[22px] text-heading mb-[30px]">About Orbis Property</h5>
              <div class="about_detail pl-[20px]">
                <h5>What's happening in the area</h5>
                <ul class="list-disc">
                  <li>Distance from city (km) - Just 40 minutes to Melbourne’s CBD with great connectivity via major roads. 35 kilometers from Melbourne CBD</li>
                  <li>Comparison to house -</li>
                  <li>Transport infrastructure - Melton and Rockbank train stations within 10 minutes (28-minute commute to CBD)</li>
                  <li>
                    Growth corridor:
                    <ul class="list-decimal pl-[20px]">
                      <li> Western Highway Upgrade - Linking Melbourne and Adelaide, the $672 million Western Highway Upgrade is being implemented to meet the demands of a growing population.</li>
                      <li>West Gate Tunnel Project - Government forecasts estimate this $6.7 billion project connecting Yarraville with the Docklands and removing thousands of trucks from residential areas, will create over 6,000 new jobs.</li>
                      <li>Werribee Employment Precinct - This $70 million project will create a thriving</li>
                    </ul>
                  </li>
                </ul>
                <div class="more_link text-primary font-medium"><a href="#">Read More</a></div>
              </div>
            </div>
        </div>
    </div>
</template>
<script>
import { Button, createResource } from 'frappe-ui'
import Tabs from '../components/Tabs.vue'
import Images from '../components/images.vue'
import Details from '../components/ProjectDetails/index.vue'
import Documents from '../components/Documents.vue'
import Location from '../components/Location.vue'
import stagedetail from '../data/stagedetails.json';
import StockList from '../components/ProjectDetails/StockList.vue'
export default {
    name: 'StageDetail',
    components: {
    Images,
    Details,
    Tabs,
    Button,
    Documents,
    Location,
    StockList
},
    data() {
    return {
      showTabs: false,
      project_detail: {},
      projectSummury:{
        available: '',
        sold: '',
        reserved: '',
        totalAllocation: ''      
      },
      project_location: { lat: 40.689247, lng: -74.044502 },
      images: [],
      featured_image: '',
      tabs: stagedetail.tabs,
      stocktableColumns: stagedetail.stocktableColumns,
      stocktableData: [],
    }
  },
  methods: {
    getdata() {
      const data = createResource({
        method: 'Get',
        url: `opssalesportal.api.realestate_project.get_project_details?project=${this.$route.params.id}`
      })
        return data.reload()
      },
    handleScroll() {
      // Define the scroll threshold in pixels, adjust this value as needed
      const scrollThreshold = 700;
      // Check the scroll position
      if (window.scrollY >= scrollThreshold) {
        this.showTabs = true;
      } else {
        this.showTabs = false;
      }
      console.log(this.showTabs);
    },
  },
  async mounted() {
    const response = await this.getdata();
    this.project_detail = response.projectdetails
    this.featured_image = this.project_detail.featured_image
    this.images = [{ 'image': this.project_detail.featured_image }, ...this.project_detail.project_images]
    this.projectSummury.available = response.availabel
    this.projectSummury.reserved = response.reserved
    this.projectSummury.sold = response.sold
    this.projectSummury.totalAllocation = response.totalAllocation
    if (this.project_detail?.coordinate) {
      let coordinate = JSON.parse(this.project_detail.coordinate).features[0].geometry.coordinates;
      this.project_location = {
        lat: coordinate[1],
        lng: coordinate[0]
      }
    }
    window.addEventListener("scroll", this.handleScroll); 
  }
}
</script>