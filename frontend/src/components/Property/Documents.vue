<template>
    <div class="md:pt-[25px] pt-[20px] md:pb-[30px] pb-[20px] border-b">
        <div class="document-comp max-w-[1780px] m-auto">
            <div class="title_btn sm:flex xs:block block justify-between items-center mb-[30px]">
                <div class="comp_title font-medium text-[22px] text-heading sm:mb-0 xs:mb-3 mb-3">Property Document</div>
                <div class="download_btn">
                    <Button variant="solid" size="lg" label="Download All Files" theme="primary"
                        class="bg-primary text-white px-[30px]" />
                </div>
            </div>
            <div class="documents flex flex-wrap items-cnter gap-[40px]">
                <div v-for="item in [1, 2, 3, 4, 5]" :key="item.index" class="doc_box bg-[#F6F7F8] p-[30px] flex flex-col items-center rounded-sm">
                    <div class="doc_image mb-[25px]">
                        <svg xmlns="http://www.w3.org/2000/svg" width="75" height="100" viewBox="0 0 75 100" fill="none">
                            <path
                                d="M35.5273 50.0195C34.5508 46.8945 34.5703 40.8594 35.1367 40.8594C36.7773 40.8594 36.6211 48.0664 35.5273 50.0195ZM35.1953 59.2383C33.6914 63.1836 31.8164 67.6953 29.6484 71.4844C33.2227 70.1172 37.2656 68.125 41.9336 67.207C39.4531 65.332 37.0703 62.6367 35.1953 59.2383ZM16.8164 83.6133C16.8164 83.7695 19.3945 82.5586 23.6328 75.7617C22.3242 76.9922 17.9492 80.5469 16.8164 83.6133ZM48.4375 31.25H75V95.3125C75 97.9102 72.9102 100 70.3125 100H4.6875C2.08984 100 0 97.9102 0 95.3125V4.6875C0 2.08984 2.08984 0 4.6875 0H43.75V26.5625C43.75 29.1406 45.8594 31.25 48.4375 31.25ZM46.875 64.8047C42.9688 62.4219 40.3711 59.1406 38.5352 54.2969C39.4141 50.6836 40.8008 45.1953 39.7461 41.7578C38.8281 36.0156 31.4648 36.582 30.4102 40.4297C29.4336 44.0039 30.332 49.043 31.9922 55.4688C29.7266 60.8594 26.3867 68.0859 24.0234 72.2266C24.0039 72.2266 24.0039 72.2461 23.9844 72.2461C18.6914 74.9609 9.60938 80.9375 13.3398 85.5273C14.4336 86.875 16.4648 87.4805 17.5391 87.4805C21.0352 87.4805 24.5117 83.9648 29.4727 75.4102C34.5117 73.75 40.0391 71.6797 44.9023 70.8789C49.1406 73.1836 54.1016 74.6875 57.4023 74.6875C63.1055 74.6875 63.4961 68.4375 61.25 66.2109C58.5352 63.5547 50.6445 64.3164 46.875 64.8047ZM73.6328 20.5078L54.4922 1.36719C53.6133 0.488281 52.4219 0 51.1719 0H50V25H75V23.8086C75 22.5781 74.5117 21.3867 73.6328 20.5078ZM59.1602 70.3711C59.9609 69.8438 58.6719 68.0469 50.8008 68.6133C58.0469 71.6992 59.1602 70.3711 59.1602 70.3711Z"
                                fill="#596263" />
                        </svg>
                    </div>
                    <div class="doc_name text-heading">orbis-property-1.pdf</div>
                    <div class="download_link text-primary"><a href="">Download Now</a></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { Button } from 'frappe-ui'
export default {
    name: 'Propertydocumets',
    components: {
        Button
    }
}
</script>