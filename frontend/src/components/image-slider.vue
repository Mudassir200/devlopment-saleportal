<template>
    <div class="thumbnail-slider">
    <Carousel id="gallery" :items-to-show="1" :wrap-around="false" v-model="currentSlide" class="mb-[10px]">
      <Slide v-for="(slide,key) in images" :key="key">
        <div class="carousel__item"><img :src="slide.image" class="xl:min-h-[573px] h-full object-cover" /></div>
      </Slide>
    </Carousel>
  
    <Carousel
      id="thumbnails"
      :items-to-show="4"
      :wrap-around="true"
      v-model="currentSlide"
      ref="carousel"
    >
      <Slide v-for="(slide,key) in images" :key="key">
        <div class="carousel__item px-[5px] h-full" @click="slideTo(key - 1)" ><img :src="slide.image" class="h-full"/></div>
      </Slide>
    </Carousel>
</div>
  </template>
  
  <script>
  import { defineComponent } from 'vue'
  import { Carousel, Slide } from 'vue3-carousel'
  
  import 'vue3-carousel/dist/carousel.css'
  
  export default defineComponent({
    name: 'ImageSlider',
    components: {
      Carousel,
      Slide,
      Navigation,
    },
    props: {
      image: String,
      images: Array
    },
    data: () => ({
      currentSlide: 0,
      slides: []
    }),
    methods: {
      slideTo(val) {
        this.currentSlide = val
      },
    },
    mounted(){
      console.log(this.images);
    }
  })
  </script>
  