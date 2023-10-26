<template>
  <div class="detail">
    <div class="flex justify-between gap-[15px] flex-wrap mb-[15px]">
      <div class="flex flex-wrap items-center gap-x-[15px] gap-y-[10px]">
        <div class="xl:text-[30px] lg:text-[25px] md:text-[20px] text-[20px] text-heading font-bold">
          {{property_detail.property_name}}
        </div>
        <div class="flex items-center gap-[18px]">
          <div class="text-body_text">{{property_detail.property_type}}</div>
          <div class="">
            <svg xmlns="http://www.w3.org/2000/svg" height="6px" viewBox="0 0 512 512" class="fill-body_text">
              <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
            </svg>
          </div>
          <div class="text-body_text">{{property_detail.contract_type}}</div>
        </div>
        <Badge :variant="'solid'" theme="primary" size="lg" class="bg-[#0078B9] text-white pl-[25px] pr-[25px]">{{property_detail.property_status}}</Badge>
      </div>
      <div class="flex items-center gap-[10px]">
        <button :variant="'solid'" theme="white" size="lg">
          <svg xmlns="http://www.w3.org/2000/svg" width="42" height="42" viewBox="0 0 42 42" fill="none">
            <rect width="42" height="42" rx="7" fill="#F2F2F2" />
            <path
              d="M12.8519 27.3024L13.6987 28.7649C13.8746 29.0729 14.1275 29.3148 14.4244 29.4908C15.2749 28.4112 15.8668 27.5828 16.2004 27.0055C16.5389 26.4197 16.9549 25.5033 17.4485 24.2564C16.1183 24.0813 15.1103 23.9937 14.4245 23.9937C13.7662 23.9937 12.7583 24.0813 11.4004 24.2564C11.4004 24.5973 11.4884 24.9381 11.6643 25.2461L12.8519 27.3024Z"
              fill="#0066DA" />
            <path
              d="M27.5763 29.4908C27.8733 29.3148 28.1262 29.0729 28.3021 28.765L28.654 28.1602L30.3365 25.2461C30.5092 24.9448 30.6002 24.6036 30.6004 24.2564C29.2347 24.0813 28.2285 23.9937 27.5819 23.9937C26.8869 23.9937 25.8807 24.0813 24.5633 24.2564C25.051 25.5101 25.4616 26.4265 25.7949 27.0055C26.1312 27.5897 26.7249 28.418 27.5763 29.4908Z"
              fill="#EA4335" />
            <path
              d="M21.0004 18.0983C21.9844 16.9099 22.6625 15.9935 23.0348 15.3492C23.3345 14.8303 23.6645 14.0019 24.0245 12.8639C23.7275 12.6879 23.3867 12.6 23.0348 12.6H18.966C18.6142 12.6 18.2734 12.699 17.9764 12.8639C18.4343 14.169 18.8229 15.0979 19.1421 15.6504C19.4949 16.2611 20.1144 17.077 21.0004 18.0983Z"
              fill="#00832D" />
            <path
              d="M24.5523 24.2564L17.4485 24.2564L14.4244 29.4908C14.7213 29.6667 15.0622 29.7547 15.4141 29.7547H26.5866C26.9385 29.7547 27.2795 29.6558 27.5763 29.4908L24.5523 24.2564Z"
              fill="#2684FC" />
            <path
              d="M21.0004 18.0983L17.9764 12.8639C17.6794 13.0398 17.4265 13.2818 17.2506 13.5897L11.6643 23.2667C11.4916 23.568 11.4006 23.9091 11.4004 24.2564H17.4485L21.0004 18.0983Z"
              fill="#00AC47" />
            <path
              d="M27.5434 18.4282L24.7502 13.5897C24.5743 13.2817 24.3214 13.0398 24.0245 12.8639L21.0004 18.0983L24.5523 24.2564H30.5894C30.5894 23.9154 30.5015 23.5746 30.3255 23.2667L27.5434 18.4282Z"
              fill="#FFBA00" />
          </svg>
        </button>
        <Button :variant="'solid'" theme="primary" size="lg"
          class="bg-primary text-white px-[25px] py-[8px] rounded-[5px]" @click="reserveOpen = true">
          Reserve Now
        </Button>
        <Dialog v-model="reserveOpen" class="p-[50px]">
          <template #body-title>
            <h3 class="text-heading text-[26px] font-bold">Confirm and Reserve Property</h3>
          </template>
          <template #body-content>
            <div class="flex flex-col gap-[25px]">
              <div class="field flex-auto">
                <FormControl type="select" placeholder="Placeholder" label="Select Customer" size="lg"
                  :options="contract_type" variant="outline" />
              </div>
              <div class="field flex-auto">
                <FormControl type="select" placeholder="Placeholder" label="Buyer Type" size="lg" :options="buyer_type"
                  v-model="buyer_type.value" variant="outline" />
              </div>
              <div class="field flex-auto">
                <FormControl type="select" placeholder="Placeholder" label="Deposit Type" size="lg"
                  :options="deposit_type" v-model="deposit_type.value" variant="outline" />
              </div>
              <div class="field flex-auto">
                <div class="font-medium text-lg text-heading mb-[15px]">Acceptable Buyer Types:</div>
                <FormControl type="checkbox" label="Purchaser Must Be - Owner-Occupier, Investor, SMSF, Trust"
                  v-model="purchaser_must_be" size="sm" class="pb-[7px]" />
              </div>
            </div>
          </template>
          <template #actions>
            <Button variant="solid" theme="primary" size="lg" class="bg-primary text-white">
              Reserve Property
            </Button>
          </template>
        </Dialog>

      </div>
    </div>
    <p class="text-body_text md:text-[18px] sm:text-[16px] text-[14px] md:mb-[30px] mb-[20px]">
      {{project_detail.full_address}}
    </p>
    <div class="justify-between xl:w-[80%] lg:w-full w-full md:pb-[30px] pb-[20px] sm:flex xs:block block">
      <div class="flex place-items-center sm:mb-0 xs:mb-2 mb-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="14" viewBox="0 0 16 10" fill="none">
          <path
            d="M4.4 4.8C5.50275 4.8 6.4 3.90275 6.4 2.8C6.4 1.69725 5.50275 0.8 4.4 0.8C3.29725 0.8 2.4 1.69725 2.4 2.8C2.4 3.90275 3.29725 4.8 4.4 4.8ZM13.2 1.6H7.6C7.379 1.6 7.2 1.779 7.2 2V5.6H1.6V0.4C1.6 0.179 1.421 0 1.2 0H0.4C0.179 0 0 0.179 0 0.4V9.2C0 9.421 0.179 9.6 0.4 9.6H1.2C1.421 9.6 1.6 9.421 1.6 9.2V8H14.4V9.2C14.4 9.421 14.579 9.6 14.8 9.6H15.6C15.821 9.6 16 9.421 16 9.2V4.4C16 2.8535 14.7465 1.6 13.2 1.6Z"
            fill="#596263" />
        </svg>
        <p class="text-body_text text-base ml-3">
          Beds: <span class="text-black font-bold">{{property_detail.bedrooms}}</span>
        </p>
      </div>
      <div class="flex place-items-center sm:mb-0 xs:mb-2 mb-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="14" viewBox="0 0 16 14" fill="none">
          <path
            d="M12.1769 3.2375L7.2375 8.17688C6.94469 8.46969 6.46969 8.46969 6.17688 8.17688L5.82312 7.82312C5.53031 7.53031 5.53031 7.05531 5.82312 6.7625L5.82656 6.75906C4.76312 5.5025 4.72781 3.66719 5.72062 2.37219C5.34656 2.13625 4.90375 2 4.43 2C3.09 2 2 3.09 2 4.43V14H0V4.43C0 1.98719 1.98719 0 4.43 0C5.58406 0 6.63656 0.44375 7.42562 1.16937C8.5475 0.809687 9.81625 1.02875 10.7591 1.82656L10.7625 1.82312C11.0553 1.53031 11.5303 1.53031 11.8231 1.82312L12.1769 2.17688C12.4697 2.46969 12.4697 2.94469 12.1769 3.2375ZM12 5.5C12 5.77616 11.7762 6 11.5 6C11.2238 6 11 5.77616 11 5.5C11 5.22384 11.2238 5 11.5 5C11.7762 5 12 5.22384 12 5.5ZM13 5.5C13 5.22384 13.2238 5 13.5 5C13.7762 5 14 5.22384 14 5.5C14 5.77616 13.7762 6 13.5 6C13.2238 6 13 5.77616 13 5.5ZM16 5.5C16 5.77616 15.7762 6 15.5 6C15.2238 6 15 5.77616 15 5.5C15 5.22384 15.2238 5 15.5 5C15.7762 5 16 5.22384 16 5.5ZM11 6.5C11 6.77616 10.7762 7 10.5 7C10.2238 7 10 6.77616 10 6.5C10 6.22384 10.2238 6 10.5 6C10.7762 6 11 6.22384 11 6.5ZM12.5 6C12.7762 6 13 6.22384 13 6.5C13 6.77616 12.7762 7 12.5 7C12.2238 7 12 6.77616 12 6.5C12 6.22384 12.2238 6 12.5 6ZM15 6.5C15 6.77616 14.7762 7 14.5 7C14.2238 7 14 6.77616 14 6.5C14 6.22384 14.2238 6 14.5 6C14.7762 6 15 6.22384 15 6.5ZM10 7.5C10 7.77616 9.77616 8 9.5 8C9.22384 8 9 7.77616 9 7.5C9 7.22384 9.22384 7 9.5 7C9.77616 7 10 7.22384 10 7.5ZM11 7.5C11 7.22384 11.2238 7 11.5 7C11.7762 7 12 7.22384 12 7.5C12 7.77616 11.7762 8 11.5 8C11.2238 8 11 7.77616 11 7.5ZM14 7.5C14 7.77616 13.7762 8 13.5 8C13.2238 8 13 7.77616 13 7.5C13 7.22384 13.2238 7 13.5 7C13.7762 7 14 7.22384 14 7.5ZM10 8.5C10 8.22384 10.2238 8 10.5 8C10.7762 8 11 8.22384 11 8.5C11 8.77616 10.7762 9 10.5 9C10.2238 9 10 8.77616 10 8.5ZM13 8.5C13 8.77616 12.7762 9 12.5 9C12.2238 9 12 8.77616 12 8.5C12 8.22384 12.2238 8 12.5 8C12.7762 8 13 8.22384 13 8.5ZM10 9.5C10 9.77616 9.77616 10 9.5 10C9.22384 10 9 9.77616 9 9.5C9 9.22384 9.22384 9 9.5 9C9.77616 9 10 9.22384 10 9.5ZM12 9.5C12 9.77616 11.7762 10 11.5 10C11.2238 10 11 9.77616 11 9.5C11 9.22384 11.2238 9 11.5 9C11.7762 9 12 9.22384 12 9.5ZM11 10.5C11 10.7762 10.7762 11 10.5 11C10.2238 11 10 10.7762 10 10.5C10 10.2238 10.2238 10 10.5 10C10.7762 10 11 10.2238 11 10.5ZM10 11.5C10 11.7762 9.77616 12 9.5 12C9.22384 12 9 11.7762 9 11.5C9 11.2238 9.22384 11 9.5 11C9.77616 11 10 11.2238 10 11.5Z"
            fill="#596263" />
        </svg>
        <p class="text-body_text text-base ml-3">
          Baths: <span class="text-black font-bold">{{property_detail.bathrooms}}</span>
        </p>
      </div>
      <div class="flex place-items-center sm:mb-0 xs:mb-2 mb-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="14" viewBox="0 0 16 12" fill="none">
          <path
            d="M15.6246 3.5H13.7537L13.2337 2.2C12.6993 0.863438 11.424 0 9.98427 0H6.01552C4.57614 0 3.30052 0.863438 2.76583 2.2L2.24583 3.5H0.375199C0.131137 3.5 -0.0479262 3.72938 0.0114489 3.96594L0.198949 4.71594C0.240512 4.88282 0.390512 5.00001 0.5627 5.00001H1.18989C0.7702 5.36657 0.499887 5.89938 0.499887 6.50001V8.00001C0.499887 8.50376 0.692387 8.95845 0.999888 9.31032V11C0.999888 11.5522 1.4477 12 1.99989 12H2.99989C3.55208 12 3.99989 11.5522 3.99989 11V10H11.9999V11C11.9999 11.5522 12.4477 12 12.9999 12H13.9999C14.5521 12 14.9999 11.5522 14.9999 11V9.31032C15.3074 8.95876 15.4999 8.50407 15.4999 8.00001V6.50001C15.4999 5.89938 15.2296 5.36657 14.8102 5.00001H15.4374C15.6096 5.00001 15.7596 4.88282 15.8012 4.71594L15.9887 3.96594C16.0477 3.72938 15.8687 3.5 15.6246 3.5ZM4.6227 2.94282C4.85052 2.37344 5.40208 2 6.01552 2H9.98427C10.5977 2 11.1493 2.37344 11.3771 2.94282L11.9999 4.50001H3.99989L4.6227 2.94282ZM2.99989 7.99376C2.39989 7.99376 1.99989 7.59501 1.99989 6.99688C1.99989 6.39876 2.39989 6.00001 2.99989 6.00001C3.59989 6.00001 4.49989 6.8972 4.49989 7.49532C4.49989 8.09345 3.59989 7.99376 2.99989 7.99376ZM12.9999 7.99376C12.3999 7.99376 11.4999 8.09345 11.4999 7.49532C11.4999 6.8972 12.3999 6.00001 12.9999 6.00001C13.5999 6.00001 13.9999 6.39876 13.9999 6.99688C13.9999 7.59501 13.5999 7.99376 12.9999 7.99376Z"
            fill="#596263" />
        </svg>
        <p class="text-body_text text-base ml-3">
          Carparks: <span class="text-black font-bold">{{property_detail.included_carparks}}</span>
        </p>
      </div>
      <div class="flex place-items-center sm:mb-0 xs:mb-2 mb-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="14" viewBox="0 0 16 16" fill="none">
          <path
            d="M16 4V1C16 0.447812 15.5522 0 15 0H12C11.4478 0 11 0.447812 11 1H5C5 0.447812 4.55219 0 4 0H1C0.447812 0 0 0.447812 0 1V4C0 4.55219 0.447812 5 1 5V11C0.447812 11 0 11.4478 0 12V15C0 15.5522 0.447812 16 1 16H4C4.55219 16 5 15.5522 5 15H11C11 15.5522 11.4478 16 12 16H15C15.5522 16 16 15.5522 16 15V12C16 11.4478 15.5522 11 15 11V5C15.5522 5 16 4.55219 16 4ZM13 2H14V3H13V2ZM2 2H3V3H2V2ZM3 14H2V13H3V14ZM14 14H13V13H14V14ZM13 11H12C11.4478 11 11 11.4478 11 12V13H5V12C5 11.4478 4.55219 11 4 11H3V5H4C4.55219 5 5 4.55219 5 4V3H11V4C11 4.55219 11.4478 5 12 5H13V11Z"
            fill="#596263" />
        </svg>
        <p class="text-body_text text-base ml-3">
          MPR: <span class="text-black font-bold">{{property_detail.mpr}}</span>
        </p>
      </div>
      <div class="flex place-items-center sm:mb-0 xs:mb-2 mb-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="14" viewBox="0 0 16 16" fill="none">
          <path
            d="M16 4V1C16 0.447812 15.5522 0 15 0H12C11.4478 0 11 0.447812 11 1H5C5 0.447812 4.55219 0 4 0H1C0.447812 0 0 0.447812 0 1V4C0 4.55219 0.447812 5 1 5V11C0.447812 11 0 11.4478 0 12V15C0 15.5522 0.447812 16 1 16H4C4.55219 16 5 15.5522 5 15H11C11 15.5522 11.4478 16 12 16H15C15.5522 16 16 15.5522 16 15V12C16 11.4478 15.5522 11 15 11V5C15.5522 5 16 4.55219 16 4ZM13 2H14V3H13V2ZM2 2H3V3H2V2ZM3 14H2V13H3V14ZM14 14H13V13H14V14ZM13 11H12C11.4478 11 11 11.4478 11 12V13H5V12C5 11.4478 4.55219 11 4 11H3V5H4C4.55219 5 5 4.55219 5 4V3H11V4C11 4.55219 11.4478 5 12 5H13V11Z"
            fill="#596263" />
        </svg>
        <p class="text-body_text text-base ml-3">
          Powder Room: <span class="text-black font-bold">{{ property_detail.powder_room }}</span>
        </p>
      </div>
      <div class="flex place-items-center sm:mb-0 xs:mb-2 mb-2">
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="14" viewBox="0 0 14 16" fill="none">
          <path
            d="M13.625 15H13V0.75C13 0.335781 12.6642 0 12.25 0H1.75C1.33578 0 1 0.335781 1 0.75V15H0.375C0.167906 15 0 15.1679 0 15.375V16H14V15.375C14 15.1679 13.8321 15 13.625 15ZM4 2.375C4 2.16791 4.16791 2 4.375 2H5.625C5.83209 2 6 2.16791 6 2.375V3.625C6 3.83209 5.83209 4 5.625 4H4.375C4.16791 4 4 3.83209 4 3.625V2.375ZM4 5.375C4 5.16791 4.16791 5 4.375 5H5.625C5.83209 5 6 5.16791 6 5.375V6.625C6 6.83209 5.83209 7 5.625 7H4.375C4.16791 7 4 6.83209 4 6.625V5.375ZM5.625 10H4.375C4.16791 10 4 9.83209 4 9.625V8.375C4 8.16791 4.16791 8 4.375 8H5.625C5.83209 8 6 8.16791 6 8.375V9.625C6 9.83209 5.83209 10 5.625 10ZM8 15H6V12.375C6 12.1679 6.16791 12 6.375 12H7.625C7.83209 12 8 12.1679 8 12.375V15ZM10 9.625C10 9.83209 9.83209 10 9.625 10H8.375C8.16791 10 8 9.83209 8 9.625V8.375C8 8.16791 8.16791 8 8.375 8H9.625C9.83209 8 10 8.16791 10 8.375V9.625ZM10 6.625C10 6.83209 9.83209 7 9.625 7H8.375C8.16791 7 8 6.83209 8 6.625V5.375C8 5.16791 8.16791 5 8.375 5H9.625C9.83209 5 10 5.16791 10 5.375V6.625ZM10 3.625C10 3.83209 9.83209 4 9.625 4H8.375C8.16791 4 8 3.83209 8 3.625V2.375C8 2.16791 8.16791 2 8.375 2H9.625C9.83209 2 10 2.16791 10 2.375V3.625Z"
            fill="#596263" />
        </svg>
        <p class="text-body_text text-base ml-3">
          Storeys: <span class="text-black font-bold">{{ property_detail.storeys }}</span>
        </p>
      </div>
    </div>
    <div class="border-y">
      <div
        class="justify-between leading-3 items-center sm:flex xs:block block xl:w-[70%] lg:w-full md:pt-[30px] pt-[20px] md:pb-[30px] pb-[20px]">
        <div class="flex sm:items-start xs:items-center items-center xs:mb-3 mb-3">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 14 16" fill="none">
            <path
              d="M13.625 15H13V0.75C13 0.335781 12.6642 0 12.25 0H1.75C1.33578 0 1 0.335781 1 0.75V15H0.375C0.167906 15 0 15.1679 0 15.375V16H14V15.375C14 15.1679 13.8321 15 13.625 15ZM4 2.375C4 2.16791 4.16791 2 4.375 2H5.625C5.83209 2 6 2.16791 6 2.375V3.625C6 3.83209 5.83209 4 5.625 4H4.375C4.16791 4 4 3.83209 4 3.625V2.375ZM4 5.375C4 5.16791 4.16791 5 4.375 5H5.625C5.83209 5 6 5.16791 6 5.375V6.625C6 6.83209 5.83209 7 5.625 7H4.375C4.16791 7 4 6.83209 4 6.625V5.375ZM5.625 10H4.375C4.16791 10 4 9.83209 4 9.625V8.375C4 8.16791 4.16791 8 4.375 8H5.625C5.83209 8 6 8.16791 6 8.375V9.625C6 9.83209 5.83209 10 5.625 10ZM8 15H6V12.375C6 12.1679 6.16791 12 6.375 12H7.625C7.83209 12 8 12.1679 8 12.375V15ZM10 9.625C10 9.83209 9.83209 10 9.625 10H8.375C8.16791 10 8 9.83209 8 9.625V8.375C8 8.16791 8.16791 8 8.375 8H9.625C9.83209 8 10 8.16791 10 8.375V9.625ZM10 6.625C10 6.83209 9.83209 7 9.625 7H8.375C8.16791 7 8 6.83209 8 6.625V5.375C8 5.16791 8.16791 5 8.375 5H9.625C9.83209 5 10 5.16791 10 5.375V6.625ZM10 3.625C10 3.83209 9.83209 4 9.625 4H8.375C8.16791 4 8 3.83209 8 3.625V2.375C8 2.16791 8.16791 2 8.375 2H9.625C9.83209 2 10 2.16791 10 2.375V3.625Z"
              fill="#596263" />
          </svg>
          <div class="ml-[10px] sm:block xs:flex flex xs:items-center items-center">
            <div class="sm:mb-3 xs:mb-0 mb-0">
              <span class="text-body_text font-normal text-base">Build Size Area:
              </span>
            </div>
            <div class="xs:ml-3 ml-3">
              <p class="text-black text-base font-bold">{{ property_detail.total_build_area }}</p>
            </div>
          </div>
        </div>
        <div class="flex sm:items-start xs:items-center items-center xs:mb-3 mb-3">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path
              d="M15.8534 2.64656L14.4999 1.29281C14.3124 1.10531 14.058 1 13.7927 1H8.99992V0.5C8.99992 0.22375 8.77617 0 8.49992 0H7.49992C7.22367 0 6.99992 0.22375 6.99992 0.5V1H1.74992C1.33586 1 0.999922 1.33594 0.999922 1.75V4.25C0.999922 4.66406 1.33586 5 1.74992 5H13.7927C14.058 5 14.3121 4.89469 14.4999 4.70719L15.8534 3.35375C16.0487 3.15812 16.0487 2.84188 15.8534 2.64656ZM6.99992 15.5C6.99992 15.7762 7.22367 16 7.49992 16H8.49992C8.77617 16 8.99992 15.7762 8.99992 15.5V12H6.99992V15.5ZM14.2499 7H8.99992V6H6.99992V7H2.20711C1.9418 7 1.68773 7.10531 1.49992 7.29281L0.146484 8.64656C-0.0488281 8.84188 -0.0488281 9.15844 0.146484 9.35375L1.49992 10.7072C1.68742 10.8947 1.9418 11 2.20711 11H14.2499C14.664 11 14.9999 10.6641 14.9999 10.25V7.75C14.9999 7.33594 14.664 7 14.2499 7Z"
              fill="#596263" />
          </svg>
          <div class="ml-[10px] sm:block xs:flex flex xs:items-center items-center">
            <div class="sm:mb-3 xs:mb-0 mb-0">
              <span class="text-body_text font-normal text-base">Land Size Area:
              </span>
            </div>
            <div class="xs:ml-3 ml-3">
              <p class="text-black text-base font-bold">{{ property_detail.land_size_area }}</p>
            </div>
          </div>
        </div>
        <div class="flex sm:items-start xs:items-center items-center xs:mb-3 mb-3">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path
              d="M16 4V1C16 0.447812 15.5522 0 15 0H12C11.4478 0 11 0.447812 11 1H5C5 0.447812 4.55219 0 4 0H1C0.447812 0 0 0.447812 0 1V4C0 4.55219 0.447812 5 1 5V11C0.447812 11 0 11.4478 0 12V15C0 15.5522 0.447812 16 1 16H4C4.55219 16 5 15.5522 5 15H11C11 15.5522 11.4478 16 12 16H15C15.5522 16 16 15.5522 16 15V12C16 11.4478 15.5522 11 15 11V5C15.5522 5 16 4.55219 16 4ZM13 2H14V3H13V2ZM2 2H3V3H2V2ZM3 14H2V13H3V14ZM14 14H13V13H14V14ZM13 11H12C11.4478 11 11 11.4478 11 12V13H5V12C5 11.4478 4.55219 11 4 11H3V5H4C4.55219 5 5 4.55219 5 4V3H11V4C11 4.55219 11.4478 5 12 5H13V11Z"
              fill="#596263" />
          </svg>
          <div class="ml-[10px] sm:block xs:flex flex xs:items-center items-center">
            <div class="sm:mb-3 xs:mb-0 mb-0">
              <span class="text-body_text font-normal text-base">Aspect View:
              </span>
            </div>
            <div class="xs:ml-3 ml-3">
              <p class="text-black text-base font-bold">{{property_detail.aspects_view}}</p>
            </div>
          </div>
        </div>
        <div class="flex sm:items-start xs:items-center items-center xs:mb-3 mb-3">
          <svg xmlns="http://www.w3.org/2000/svg" width="14" height="16" viewBox="0 0 14 16" fill="none">
            <path
              d="M0 14.5C0 15.3281 0.671875 16 1.5 16H12.5C13.3281 16 14 15.3281 14 14.5V6H0V14.5ZM10 8.375C10 8.16875 10.1687 8 10.375 8H11.625C11.8313 8 12 8.16875 12 8.375V9.625C12 9.83125 11.8313 10 11.625 10H10.375C10.1687 10 10 9.83125 10 9.625V8.375ZM10 12.375C10 12.1687 10.1687 12 10.375 12H11.625C11.8313 12 12 12.1687 12 12.375V13.625C12 13.8313 11.8313 14 11.625 14H10.375C10.1687 14 10 13.8313 10 13.625V12.375ZM6 8.375C6 8.16875 6.16875 8 6.375 8H7.625C7.83125 8 8 8.16875 8 8.375V9.625C8 9.83125 7.83125 10 7.625 10H6.375C6.16875 10 6 9.83125 6 9.625V8.375ZM6 12.375C6 12.1687 6.16875 12 6.375 12H7.625C7.83125 12 8 12.1687 8 12.375V13.625C8 13.8313 7.83125 14 7.625 14H6.375C6.16875 14 6 13.8313 6 13.625V12.375ZM2 8.375C2 8.16875 2.16875 8 2.375 8H3.625C3.83125 8 4 8.16875 4 8.375V9.625C4 9.83125 3.83125 10 3.625 10H2.375C2.16875 10 2 9.83125 2 9.625V8.375ZM2 12.375C2 12.1687 2.16875 12 2.375 12H3.625C3.83125 12 4 12.1687 4 12.375V13.625C4 13.8313 3.83125 14 3.625 14H2.375C2.16875 14 2 13.8313 2 13.625V12.375ZM12.5 2H11V0.5C11 0.225 10.775 0 10.5 0H9.5C9.225 0 9 0.225 9 0.5V2H5V0.5C5 0.225 4.775 0 4.5 0H3.5C3.225 0 3 0.225 3 0.5V2H1.5C0.671875 2 0 2.67188 0 3.5V5H14V3.5C14 2.67188 13.3281 2 12.5 2Z"
              fill="#596263" />
          </svg>
          <div class="ml-[10px] sm:block xs:flex flex xs:items-center items-center">
            <div class="sm:mb-3 xs:mb-0 mb-0">
              <span class="text-body_text font-normal text-base">Dev. Est. Settl. Date:
              </span>
            </div>
            <div class="xs:ml-3 ml-3">
              <p class="text-black text-base font-bold">{{ project_detail.project_enddate }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="md:pt-[30px] pt-[20px] md:pb-[30px] pb-[20px]">
      <h5 class="md:pb-[30px] pb-[20px] text-[22px] font-bold text-gray-800">
        Important Information
      </h5>
      <div class="md:flex sm:block block">
        <div class="lg:w-2/5 md:w-full w-full xl:border-r lg:border-r-none lg:mb-0 md:mb-7 mb-7">
          <div class="w-full">
            <h5 class="mb-5 text-lg font-normal text-primary">
              Property Cashflow Information
            </h5>
            <div class="items-center w-full sm:flex xs:block block mb-5">
              <div
                class="justify-between sm:leading-9 xs:leading-1 leading-1 sm:w-6/12 xs:w-full w-full sm:block xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                <div class="mb-0">
                  <div class="flex place-items-center">
                    <p class="text-black text-base font-medium">
                      Est. Rents (p.w.):
                    </p>
                  </div>
                  <div class="mb-0">
                    <span class="text-gray-500 font-normal text-base">{{ property_detail.estimated_rent }}</span>
                  </div>
                </div>
              </div>
              <div
                class="justify-between sm:leading-9 xs:leading-1 leading-1 sm:w-6/12 xs:w-full w-full sm:block xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                <div class="mb-0">
                  <div class="flex place-items-center">
                    <p class="text-black text-base font-medium">
                      Water Rates (p.a.):
                    </p>
                  </div>
                  <div class="mb-0">
                    <span class="text-gray-500 font-normal text-base">{{ property_detail.estimated_water_rates }}</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="place-items-center w-full sm:flex xs:block block mb-5">
              <div
                class="justify-between sm:leading-9 xs:leading-1 leading-1 sm:w-6/12 xs:w-full w-full sm:block xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                <div class="mb-0">
                  <div class="flex place-items-center">
                    <p class="text-black text-base font-medium">
                      Rental Yield:
                    </p>
                  </div>
                  <div class="mb-0">
                    <span class="text-gray-500 font-normal text-base">{{ property_detail.rental_yield }}</span>
                  </div>
                </div>
              </div>
              <div
                class="justify-between sm:leading-9 xs:leading-1 leading-1 sm:w-6/12 xs:w-full w-full sm:block xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                <div class="mb-0">
                  <div class="flex place-items-center">
                    <p class="text-black text-base font-medium">
                      Owner Corp (p.w.):
                    </p>
                  </div>
                  <div class="mb-0">
                    <span class="text-gray-500 font-normal text-base">A$1,000</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="place-items-center w-full sm:flex xs:block block">
              <div
                class="justify-between sm:leading-9 xs:leading-1 leading-1 sm:w-6/12 xs:w-full w-full sm:block xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                <div class="mb-0">
                  <div class="flex place-items-center">
                    <p class="text-black text-base font-medium">
                      Council Rates (p.a.):
                    </p>
                  </div>
                  <div class="mb-0">
                    <span class="text-gray-500 font-normal text-base">{{ property_detail.estimated_council_rates }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="lg:w-3/5 md:w-full w-full lg:ml-[80px] md:ml-[0px] ml-[0px]">
          <div class="w-full">
            <h5 class="mb-5 text-base font-normal text-primary">
              Property Cashflow Information
            </h5>
            <div class="place-items-center w-full sm:flex xs:block block mb-5">
              <div class="place-items-center w-full sm:flex xs:block block">
                <div
                  class="justify-between sm:leading-9 xs:leading-1 leading-1 sm:block xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                  <div class="mb-0">
                    <p class="text-black text-base font-medium">
                      Reservation Deposit Amount:
                    </p>
                    <div class="mb-0">
                      <span class="text-gray-500 font-normal text-base">{{ project_detail.holding_deposit }}</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="place-items-center w-full sm:flex xs:block block">
                <div class="justify-between sm:leading-9 xs:leading-1 leading-1 xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                  <div class="mb-0">
                    <p class="text-black text-base font-medium">
                      Land Balance Deposit Amount:
                    </p>
                    <div class="mb-0">
                      <span class="text-gray-500 font-normal text-base">{{ property_detail.land_balance_deposit }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="place-items-center w-full sm:flex xs:block block">
              <div class="place-items-center w-full sm:flex xs:block block">
                <div class="justify-between sm:leading-9 xs:leading-1 leading-1 xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                  <div class="mb-0">
                    <p class="text-black text-base font-medium">
                      House Balance Deposit Amount:
                    </p>
                    <div class="mb-0">
                      <span class="text-gray-500 font-normal text-base">{{ property_detail.house_balance_deposit }}</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="place-items-center w-full sm:flex xs:block block">
                <div class="justify-between sm:leading-9 xs:leading-1 leading-1 xs:flex flex sm:mb-0 xs:mb-2 mb-2">
                  <div class="mb-0">
                    <p class="text-black text-base font-medium">
                      Allowed Buyer Type:
                    </p>
                    <div class="mb-0">
                      <span class="text-gray-500 font-normal text-base">{{ property_detail?.allowed_buyer_type || "null" }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="md:pt-[30px] pt-[20px] md:pb-[30px] pb-[20px] border-y">
      <h5 class="md:pb-[30px] pb-[20px] text-[22px] font-bold text-gray-800">
        About Property
      </h5>
      <p class="text-body_text font-normal text-base leading-7">{{ project_detail.description }}</p>
      <a href="" class="text-primary font-medium">Read More</a>
    </div>
  </div>
</template>


<script>
import { Button, Dialog, FormControl, Badge } from 'frappe-ui'
export default {
  name: 'Details',
  components: {
    Button,
    FormControl,
    Dialog,
    Badge
  },
  data() {
    return {
      reserveOpen: false,
      purchaser_must_be: false,
      contract_type: [
        { label: 'One Part', value: 'one_part' },
        { label: 'Two Part', value: 'two_part' },
      ],
      deposit_type: [
        { label: 'Cash', value: 'cash' },
        { label: 'Personal Loan', value: 'personal_loan' },
        { label: 'Refinance', value: 'refinance' },
        { label: 'SMSF', value: 'smsf' },
      ],
      buyer_type: [
        { label: 'Investor', value: 'investor' },
        { label: 'Owner Occupier', value: 'owner_occupier' },
      ],
    }
  },
  props: {
        property_detail: Object,
        project_detail: Object
    }
}
</script>