<template>
  <div class="md:pt-[25px] pt-[20px]">
    <div class="location-comp max-w-[1780px] m-auto">
        <div class="title_btn sm:flex xs:block block justify-between items-center mb-[30px]">
            <div class="comp_title font-medium text-[22px] text-heading">Location</div>
            <div class="address_box">
                <div class="addres text-body_text">Orbis Property, VIC 3338 Australia</div>
            </div>
        </div>
        <GoogleMap api-key="AIzaSyDpPcBtSaGdqT9_Uuk9B5r84rXh2xGqh3M" style="width: 100%; height: 500px" :center="center" :zoom="15">
        <Marker :options="{ position: center }" />
        </GoogleMap>
    </div>
  </div>
  </template>
  
  <script>
  import { defineComponent } from "vue";
  import { GoogleMap, Marker } from "vue3-google-map";
  
  export default defineComponent({
    name: 'Propertymap',
    components: { GoogleMap, Marker },
    setup() {
      const center = { lat: 40.689247, lng: -74.044502 };
  
      return { center };
    },
  });
  </script>