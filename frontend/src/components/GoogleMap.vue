<template>
    <div>
      <GoogleMap
        :center="center"
        :zoom="13"
        style="width: 100%; height: 100vh"
        api-key="AIzaSyDpPcBtSaGdqT9_Uuk9B5r84rXh2xGqh3M"
      >
        <Marker
          v-for="(marker, index) in markers"
          :key="index"
          :options="{ position: marker.position }"
          @mouseover="showInfoWindow(index)"
          @mouseout="hideInfoWindow(index)"
        >
        <InfoWindow
          :visible="marker.showInfoWindow"
        >
        {{ marker.infoWindowContent }}
    </InfoWindow>
        </Marker>
      </GoogleMap>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { GoogleMap, Marker, InfoWindow } from 'vue3-google-map';
  
  export default {
    name:"GoogleMaps",
    components: {
        GoogleMap,
        Marker,
        InfoWindow,
    },
    setup() {
      const center = ref({ lat: 40.689247, lng: -74.044502 });
      const markers = ref([
        {
          position: { lat: 40.689247, lng: -74.044502 },
          showInfoWindow: true,
          infoWindowContent: 'Info Window 1',
        },
        // Add more markers as needed
      ]);
  
      const showInfoWindow = (index) => {
        markers.value[index].showInfoWindow = true;
      };
  
      const hideInfoWindow = (index) => {
        markers.value[index].showInfoWindow = false;
      };
  
      return { center, markers, showInfoWindow, hideInfoWindow };
    },
  };
  </script>
  