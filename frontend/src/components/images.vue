<template>
  <div class="images_comp">
    <div class="banner-section">
      <div class="property_images-container grid lg:grid-cols-2 md:grid-cols-1 grid-cols-1 gap-[10px]">
        <div class="featured_image">
          <img :src="featuredImage" alt="featured_image" class="h-full object-cover w-full" />
        </div>
        <div class="property_images grid grid-cols-2 gap-[10px]">
          <div v-for="(item, index) in images" :key="item.index" v-show="index < 4" class="property_image relative max-h-[344.09px]">
            <div v-if="index == 3" class="overlay absolute inset-0 bg-[#000] opacity-50"></div>
            <a :href="item.image" :data-fancybox="'gallery'">
              <div v-if="index == 3" class="overlay absolute top-1/2 left-1/2 text-white translate-x-[-50%]">
                View All Images
              </div>
            </a>
              <img :src="item.image" alt="" class="w-full h-full object-cover h-full"/>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import "@fancyapps/fancybox/dist/jquery.fancybox.min.css" // Import Fancybox CSS
import "@fancyapps/fancybox/dist/jquery.fancybox.min.js" // Import Fancybox JS
export default {
  name: 'Images',
  mounted() {
    this.initializeFancybox();
  },
  methods: {
    initializeFancybox() {
      const galleryImages = document.querySelectorAll("[data-fancybox^='gallery']");
      $(galleryImages).fancybox({
        type: "image",
        spinnerTpl: false, // Disable the loading spinner
      });
    },
  },
  props: {
    featuredImage: String,
    images: Array
  }
}
</script>