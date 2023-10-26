<template>
  <div class="location-comp max-w-[1780px] m-auto">
    <div class="title_btn flex justify-between items-center mb-[30px]">
      <div class="comp_title font-medium text-[22px] text-heading">Location</div>
      <div class="address_box">
        <div class="addres text-body_text">{{ project_detail.full_address }}</div>
      </div>
    </div>
    <GoogleMap api-key="AIzaSyDpPcBtSaGdqT9_Uuk9B5r84rXh2xGqh3M" style="width: 100%; height: 500px"
      :center="project_location" :zoom="15">
      <Marker :options="{ position: project_location }">
        <InfoWindow class="p-0">
          <ProjectCard class="max-w-[350px] w-full bg-white border border-gray-200 rounded-[10px]"
            :project="project_detail" :infowindow="true" />
        </InfoWindow>
      </Marker>
    </GoogleMap>
  </div>
</template>
  
<script>
import { defineComponent } from "vue";
import { GoogleMap, Marker, InfoWindow } from "vue3-google-map";
import ProjectCard from "./ProjectCard.vue";

export default defineComponent({
  name: 'location',
  components: { GoogleMap, Marker, ProjectCard, InfoWindow },
  props: {
    project_detail: Object,
    project_location: Object
  }
});
</script>