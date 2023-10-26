<template>
    <div class="detail_comp">
        <div class="flex justify-between mb-[30px] flex-wrap gap-[20px]">
            <div class="general_deatil">
                <div class="flex items-center flex-wrap gap-[15px]">
                    <div class="project_name md:text-[36px] sm:text-[25px] text-[20px] text-heading font-bold">
                        {{ project_detail.project_name }}</div>
                    <div class="flex items-center gap-[15px]">
                        <div class="project_items text-body_text">{{ project_detail.property_type }}</div>
                        <div class="">
                            <svg xmlns="http://www.w3.org/2000/svg" height="6px" viewBox="0 0 512 512"
                                class="fill-body_text">
                                <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512z" />
                            </svg>
                        </div>
                        <div class="contract_type text-body_text">{{ project_detail.contract_type }}</div>
                    </div>
                </div>
                <div class="address_box flex gap-[10px] items-center md:mb-[30px] mb-[20px]">
                    <div class="address_icon">
                        <svg xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 384 512"
                            class="fill-body_text w-[12px]">
                            <path
                                d="M215.7 499.2C267 435 384 279.4 384 192C384 86 298 0 192 0S0 86 0 192c0 87.4 117 243 168.3 307.2c12.3 15.3 35.1 15.3 47.4 0zM192 128a64 64 0 1 1 0 128 64 64 0 1 1 0-128z" />
                        </svg>
                    </div>
                    <div class="address text-body_text md:text-[20px] sm:text-[16px] text-[14px]">
                        {{ project_detail.full_address }}</div>
                </div>
                <div class="status_badges flex xl:flex-nowrap sm:xl:flex-nowrap flex-wrap gap-[10px]">
                    <div
                        class="badge bg-[#DDF9EF] text-[#09A04F] rounded-[5px] px-[15px] py-[5px] font-medium sm:text-lg text-sm">
                        {{ projectSummury.available }} Available</div>
                    <div
                        class="badge bg-[#F9EDDD] text-[#DA5126] rounded-[5px] px-[15px] py-[5px] font-medium sm:text-lg text-sm">
                        {{ projectSummury.sold }} Sold</div>
                    <div
                        class="badge bg-[#F2F2F2] text-[#58524F] rounded-[5px] px-[15px] py-[5px] font-medium sm:text-lg text-sm">
                        {{ projectSummury.reserved }} Reserved</div>
                </div>
            </div>
            <div class="cta flex gap-[10px]">
                <div class="g_drivebtn">
                    <Button :variant="'solid'" theme="white" size="lg">
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
                    </Button>
                </div>
                <div class="master_plan_btn">
                    <Button :variant="'solid'" theme="primary" size="lg"
                        class="bg-primary text-white px-[25px] py-[8px] rounded-[5px]">View Master Plan</Button>
                </div>
            </div>
        </div>
        <div class="additional_details flex flex-wrap gap-x-[50px] gap-y-[25px] mb-[30px] py-[20px] border-y">
            <div class="detail_box">
                <div class="flex gap-[10px]">
                    <div class="detail_icon pt-[4px]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 15 14">
                        <path
                            d="M7.5 0C5.68776 0 4.21875 1.46901 4.21875 3.28125C4.21875 4.74635 6.36328 7.41667 7.1849 8.38594C7.3513 8.58229 7.64896 8.58229 7.8151 8.38594C8.63672 7.41667 10.7812 4.74635 10.7812 3.28125C10.7812 1.46901 9.31224 0 7.5 0ZM7.5 4.375C6.89583 4.375 6.40625 3.88542 6.40625 3.28125C6.40625 2.67708 6.89583 2.1875 7.5 2.1875C8.10417 2.1875 8.59375 2.67708 8.59375 3.28125C8.59375 3.88542 8.10417 4.375 7.5 4.375ZM0.523958 5.6237C0.369317 5.68555 0.236753 5.79231 0.143362 5.93022C0.049971 6.06812 3.70367e-05 6.23084 0 6.3974L0 12.9161C0 13.2109 0.297656 13.4125 0.571354 13.3031L4.16667 11.6667V5.59687C3.93646 5.18073 3.74818 4.77552 3.61328 4.38802L0.523958 5.6237ZM7.5 9.36641C7.13359 9.36641 6.78698 9.20547 6.54922 8.92474C6.03724 8.32057 5.49271 7.63255 5 6.92682V11.6664L10 13.3331V6.92708C9.50729 7.63255 8.96302 8.32083 8.45078 8.925C8.21302 9.20547 7.86641 9.36641 7.5 9.36641ZM14.4286 4.19687L10.8333 5.83333V13.3333L14.476 11.8763C14.6307 11.8145 14.7633 11.7077 14.8567 11.5698C14.9501 11.4319 15 11.2692 15 11.1026V4.58385C15 4.28906 14.7023 4.0875 14.4286 4.19687Z"
                            fill="#596263" />
                    </svg>
                </div>
                <div class="detail_title text-[body_text]">
                    Total dwellings in development:
                    <div class="detail text-heading"><b>TBD</b></div>
                </div>
                </div>
            </div>
            <div class="detail_box">
                <div class="flex gap-[10px]">
                    <div class="detail_icon pt-[4px]">
                    <svg xmlns="http://www.w3.org/2000/svg" height="15" width="15" viewBox="0 0 640 512">
                        <path
                            d="M256 64H384v64H256V64zM240 0c-26.5 0-48 21.5-48 48v96c0 26.5 21.5 48 48 48h48v32H32c-17.7 0-32 14.3-32 32s14.3 32 32 32h96v32H80c-26.5 0-48 21.5-48 48v96c0 26.5 21.5 48 48 48H240c26.5 0 48-21.5 48-48V368c0-26.5-21.5-48-48-48H192V288H448v32H400c-26.5 0-48 21.5-48 48v96c0 26.5 21.5 48 48 48H560c26.5 0 48-21.5 48-48V368c0-26.5-21.5-48-48-48H512V288h96c17.7 0 32-14.3 32-32s-14.3-32-32-32H352V192h48c26.5 0 48-21.5 48-48V48c0-26.5-21.5-48-48-48H240zM96 448V384H224v64H96zm320-64H544v64H416V384z"
                            fill="#596263" />
                    </svg>
                </div>
                <div class="detail_title text-[body_text]">
                    Total Allocation:
                    <div class="detail text-heading"><b>{{ projectSummury.totalAllocation }}</b></div>
                </div>
                </div>
            </div>
            <div v-if="project_detail.multistage == 0" class="detail_box">
                <div class="flex gap-[10px]">
                    <div class="detail_icon pt-[4px]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="9" height="15" viewBox="0 0 9 15" fill="none">
                        <path
                            d="M6.12784 6.83789L2.96378 5.91211C2.59757 5.80664 2.34268 5.46387 2.34268 5.08301C2.34268 4.60547 2.7294 4.21875 3.20694 4.21875H5.14932C5.50675 4.21875 5.85831 4.32715 6.15128 4.52637C6.32999 4.64648 6.57022 4.61719 6.72257 4.46777L7.7421 3.47168C7.9501 3.26953 7.92081 2.93262 7.68936 2.75391C6.97159 2.19141 6.0751 1.87793 5.15518 1.875V0.46875C5.15518 0.210938 4.94425 0 4.68643 0H3.74893C3.49112 0 3.28018 0.210938 3.28018 0.46875V1.875H3.20694C1.34073 1.875 -0.15927 3.47754 0.0135811 5.37891C0.136628 6.72949 1.16788 7.82813 2.46866 8.20898L5.47159 9.08789C5.8378 9.19629 6.09268 9.53613 6.09268 9.91699C6.09268 10.3945 5.70596 10.7812 5.22843 10.7812H3.28604C2.92862 10.7812 2.57706 10.6729 2.28409 10.4736C2.10538 10.3535 1.86514 10.3828 1.7128 10.5322L0.693269 11.5283C0.485261 11.7305 0.514558 12.0674 0.746003 12.2461C1.46378 12.8086 2.36026 13.1221 3.28018 13.125V14.5312C3.28018 14.7891 3.49112 15 3.74893 15H4.68643C4.94425 15 5.15518 14.7891 5.15518 14.5312V13.1191C6.52042 13.0928 7.80069 12.2812 8.25186 10.9893C8.88175 9.18457 7.82413 7.33301 6.12784 6.83789Z"
                            fill="#596263" />
                    </svg>
                </div>
                <div class="detail_title text-[body_text]">
                    Holding Deposit:
                    <div class="detail text-heading"><b>{{
                    project_detail.holding_deposit > 0 ? project_detail.deposit_type === "Fixed" ?
                    `$${project_detail.holding_deposit}` : `${project_detail.holding_deposit}%` : "TBA"
                }}</b></div>
                </div>
                </div>
            </div>

            <!-- Title status -->
            <div v-if="project_detail.multistage == 0 && (project_detail?.contract_type || project_detail.contract_type != 'One Part')"
                class="detail_box">
                <div class="flex gap-[10px]">
                    <div class="detail_icon pt-[4px]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="15" viewBox="0 0 12 15" fill="none">
                        <path
                            d="M9.84375 1.875H7.5C7.5 0.84082 6.65918 0 5.625 0C4.59082 0 3.75 0.84082 3.75 1.875H1.40625C0.629883 1.875 0 2.50488 0 3.28125V13.5938C0 14.3701 0.629883 15 1.40625 15H9.84375C10.6201 15 11.25 14.3701 11.25 13.5938V3.28125C11.25 2.50488 10.6201 1.875 9.84375 1.875ZM5.625 1.17188C6.01465 1.17188 6.32812 1.48535 6.32812 1.875C6.32812 2.26465 6.01465 2.57812 5.625 2.57812C5.23535 2.57812 4.92188 2.26465 4.92188 1.875C4.92188 1.48535 5.23535 1.17188 5.625 1.17188ZM9.17578 7.96289L4.98633 12.1172C4.84863 12.2549 4.62598 12.252 4.48828 12.1143L2.06836 9.67383C1.93066 9.53613 1.93359 9.31348 2.07129 9.17578L2.90332 8.34961C3.04102 8.21191 3.26367 8.21484 3.40137 8.35254L4.74902 9.71191L7.85449 6.62988C7.99219 6.49219 8.21484 6.49512 8.35254 6.63281L9.17871 7.46484C9.31641 7.60547 9.31348 7.82519 9.17578 7.96289Z"
                            fill="#596263" />
                    </svg>
                </div>
                <div class="detail_title text-[body_text]">
                    Title Status:
                    <div class="detail text-heading"><b>{{ project_detail?.title_status || "TBA" }}</b></div>
                </div>
                </div>
            </div>
            <!-- Title Date -->
            <div v-if="project_detail.multistage == 0 && (project_detail?.contract_type || project_detail.contract_type != 'One Part')"
                class="detail_box">
                <div class="flex gap-[10px]">
                    <div class="detail_icon pt-[4px]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="15" viewBox="0 0 14 15" fill="none">
                        <path d="M0 13.5938C0 14.3701 0.629883 15 1.40625 15H11.7188C12.4951 15 13.125 14.3701 13.125 13.5938V5.625H0V13.5938ZM9.375 7.85156C9.375 7.6582 9.5332 7.5 9.72656 7.5H10.8984C11.0918 7.5 11.25 7.6582 11.25 7.85156V9.02344C11.25 9.2168 11.0918 9.375 10.8984 9.375H9.72656C9.5332 9.375 9.375 9.2168 9.375 9.02344V7.85156ZM9.375 11.6016C9.375 11.4082 9.5332 11.25 9.72656 11.25H10.8984C11.0918 11.25 11.25 11.4082 11.25 11.6016V12.7734C11.25 12.9668 11.0918 13.125 10.8984 13.125H9.72656C9.5332 13.125 9.375 12.9668 9.375 12.7734V11.6016ZM5.625 7.85156C5.625 7.6582 5.7832 7.5 5.97656 7.5H7.14844C7.3418 7.5 7.5 7.6582 7.5 7.85156V9.02344C7.5 9.2168 7.3418 9.375 7.14844 9.375H5.97656C5.7832 9.375 5.625 9.2168 5.625 9.02344V7.85156ZM5.625 11.6016C5.625 11.4082 5.7832 11.25 5.97656 11.25H7.14844C7.3418 11.25 7.5 11.4082 7.5 11.6016V12.7734C7.5 12.9668 7.3418 13.125 7.14844 13.125H5.97656C5.7832 13.125 5.625 12.9668 5.625 12.7734V11.6016ZM1.875 7.85156C1.875 7.6582 2.0332 7.5 2.22656 7.5H3.39844C3.5918 7.5 3.75 7.6582 3.75 7.85156V9.02344C3.75 9.2168 3.5918 9.375 3.39844 9.375H2.22656C2.0332 9.375 1.875 9.2168 1.875 9.02344V7.85156ZM1.875 11.6016C1.875 11.4082 2.0332 11.25 2.22656 11.25H3.39844C3.5918 11.25 3.75 11.4082 3.75 11.6016V12.7734C3.75 12.9668 3.5918 13.125 3.39844 13.125H2.22656C2.0332 13.125 1.875 12.9668 1.875 12.7734V11.6016ZM11.7188 1.875H10.3125V0.46875C10.3125 0.210938 10.1016 0 9.84375 0H8.90625C8.64844 0 8.4375 0.210938 8.4375 0.46875V1.875H4.6875V0.46875C4.6875 0.210938 4.47656 0 4.21875 0H3.28125C3.02344 0 2.8125 0.210938 2.8125 0.46875V1.875H1.40625C0.629883 1.875 0 2.50488 0 3.28125V4.6875H13.125V3.28125C13.125 2.50488 12.4951 1.875 11.7188 1.875Z" fill="#596263"/>
                    </svg>
                </div>
                <div class="detail_title text-[body_text]">
                    Title Date:
                    <div class="detail text-heading"><b>{{ project_detail?.title_date || "TBA" }}</b></div>
                </div>
                </div>
            </div>
            <!-- Const Start Date: -->
            <div v-if="project_detail.multistage == 0 && project_detail?.contract_type == 'One Part'" class="detail_box">
                <div class="flex gap-[10px]">
                    <div class="detail_icon pt-[4px]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="15" viewBox="0 0 14 15" fill="none">
                        <path d="M0 13.5938C0 14.3701 0.629883 15 1.40625 15H11.7188C12.4951 15 13.125 14.3701 13.125 13.5938V5.625H0V13.5938ZM9.375 7.85156C9.375 7.6582 9.5332 7.5 9.72656 7.5H10.8984C11.0918 7.5 11.25 7.6582 11.25 7.85156V9.02344C11.25 9.2168 11.0918 9.375 10.8984 9.375H9.72656C9.5332 9.375 9.375 9.2168 9.375 9.02344V7.85156ZM9.375 11.6016C9.375 11.4082 9.5332 11.25 9.72656 11.25H10.8984C11.0918 11.25 11.25 11.4082 11.25 11.6016V12.7734C11.25 12.9668 11.0918 13.125 10.8984 13.125H9.72656C9.5332 13.125 9.375 12.9668 9.375 12.7734V11.6016ZM5.625 7.85156C5.625 7.6582 5.7832 7.5 5.97656 7.5H7.14844C7.3418 7.5 7.5 7.6582 7.5 7.85156V9.02344C7.5 9.2168 7.3418 9.375 7.14844 9.375H5.97656C5.7832 9.375 5.625 9.2168 5.625 9.02344V7.85156ZM5.625 11.6016C5.625 11.4082 5.7832 11.25 5.97656 11.25H7.14844C7.3418 11.25 7.5 11.4082 7.5 11.6016V12.7734C7.5 12.9668 7.3418 13.125 7.14844 13.125H5.97656C5.7832 13.125 5.625 12.9668 5.625 12.7734V11.6016ZM1.875 7.85156C1.875 7.6582 2.0332 7.5 2.22656 7.5H3.39844C3.5918 7.5 3.75 7.6582 3.75 7.85156V9.02344C3.75 9.2168 3.5918 9.375 3.39844 9.375H2.22656C2.0332 9.375 1.875 9.2168 1.875 9.02344V7.85156ZM1.875 11.6016C1.875 11.4082 2.0332 11.25 2.22656 11.25H3.39844C3.5918 11.25 3.75 11.4082 3.75 11.6016V12.7734C3.75 12.9668 3.5918 13.125 3.39844 13.125H2.22656C2.0332 13.125 1.875 12.9668 1.875 12.7734V11.6016ZM11.7188 1.875H10.3125V0.46875C10.3125 0.210938 10.1016 0 9.84375 0H8.90625C8.64844 0 8.4375 0.210938 8.4375 0.46875V1.875H4.6875V0.46875C4.6875 0.210938 4.47656 0 4.21875 0H3.28125C3.02344 0 2.8125 0.210938 2.8125 0.46875V1.875H1.40625C0.629883 1.875 0 2.50488 0 3.28125V4.6875H13.125V3.28125C13.125 2.50488 12.4951 1.875 11.7188 1.875Z" fill="#596263"/>
                    </svg>
                </div>
                <div class="detail_title text-[body_text]">
                    Const Start Date:
                    <div class="detail text-heading"><b>{{project_detail?.project_startdate || "TBA"}}</b></div>
                </div>
                </div>
            </div>
            <div v-else-if="project_detail.multistage == 0 && project_detail?.contract_type != 'One Part' && project_detail?.project_startdate" class="detail_box">
                <div class="flex gap-[10px]">
                    <div class="detail_icon pt-[4px]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="15" viewBox="0 0 14 15" fill="none">
                        <path d="M0 13.5938C0 14.3701 0.629883 15 1.40625 15H11.7188C12.4951 15 13.125 14.3701 13.125 13.5938V5.625H0V13.5938ZM9.375 7.85156C9.375 7.6582 9.5332 7.5 9.72656 7.5H10.8984C11.0918 7.5 11.25 7.6582 11.25 7.85156V9.02344C11.25 9.2168 11.0918 9.375 10.8984 9.375H9.72656C9.5332 9.375 9.375 9.2168 9.375 9.02344V7.85156ZM9.375 11.6016C9.375 11.4082 9.5332 11.25 9.72656 11.25H10.8984C11.0918 11.25 11.25 11.4082 11.25 11.6016V12.7734C11.25 12.9668 11.0918 13.125 10.8984 13.125H9.72656C9.5332 13.125 9.375 12.9668 9.375 12.7734V11.6016ZM5.625 7.85156C5.625 7.6582 5.7832 7.5 5.97656 7.5H7.14844C7.3418 7.5 7.5 7.6582 7.5 7.85156V9.02344C7.5 9.2168 7.3418 9.375 7.14844 9.375H5.97656C5.7832 9.375 5.625 9.2168 5.625 9.02344V7.85156ZM5.625 11.6016C5.625 11.4082 5.7832 11.25 5.97656 11.25H7.14844C7.3418 11.25 7.5 11.4082 7.5 11.6016V12.7734C7.5 12.9668 7.3418 13.125 7.14844 13.125H5.97656C5.7832 13.125 5.625 12.9668 5.625 12.7734V11.6016ZM1.875 7.85156C1.875 7.6582 2.0332 7.5 2.22656 7.5H3.39844C3.5918 7.5 3.75 7.6582 3.75 7.85156V9.02344C3.75 9.2168 3.5918 9.375 3.39844 9.375H2.22656C2.0332 9.375 1.875 9.2168 1.875 9.02344V7.85156ZM1.875 11.6016C1.875 11.4082 2.0332 11.25 2.22656 11.25H3.39844C3.5918 11.25 3.75 11.4082 3.75 11.6016V12.7734C3.75 12.9668 3.5918 13.125 3.39844 13.125H2.22656C2.0332 13.125 1.875 12.9668 1.875 12.7734V11.6016ZM11.7188 1.875H10.3125V0.46875C10.3125 0.210938 10.1016 0 9.84375 0H8.90625C8.64844 0 8.4375 0.210938 8.4375 0.46875V1.875H4.6875V0.46875C4.6875 0.210938 4.47656 0 4.21875 0H3.28125C3.02344 0 2.8125 0.210938 2.8125 0.46875V1.875H1.40625C0.629883 1.875 0 2.50488 0 3.28125V4.6875H13.125V3.28125C13.125 2.50488 12.4951 1.875 11.7188 1.875Z" fill="#596263"/>
                    </svg>
                </div>
                <div class="detail_title text-[body_text]">
                    Const Start Date:
                    <div class="detail text-heading"><b>{{project_detail.project_startdate}}</b></div>
                </div>
                </div>
            </div>
            <!-- Dev. Est. Settl. Date: -->
            <div v-if="project_detail.multistage == 0" class="detail_box">
                <div class="flex gap-[10px]">
                    <div class="detail_icon pt-[4px]">
                    <svg xmlns="http://www.w3.org/2000/svg" width="14" height="15" viewBox="0 0 14 15" fill="none">
                        <path d="M0 13.5938C0 14.3701 0.629883 15 1.40625 15H11.7188C12.4951 15 13.125 14.3701 13.125 13.5938V5.625H0V13.5938ZM9.375 7.85156C9.375 7.6582 9.5332 7.5 9.72656 7.5H10.8984C11.0918 7.5 11.25 7.6582 11.25 7.85156V9.02344C11.25 9.2168 11.0918 9.375 10.8984 9.375H9.72656C9.5332 9.375 9.375 9.2168 9.375 9.02344V7.85156ZM9.375 11.6016C9.375 11.4082 9.5332 11.25 9.72656 11.25H10.8984C11.0918 11.25 11.25 11.4082 11.25 11.6016V12.7734C11.25 12.9668 11.0918 13.125 10.8984 13.125H9.72656C9.5332 13.125 9.375 12.9668 9.375 12.7734V11.6016ZM5.625 7.85156C5.625 7.6582 5.7832 7.5 5.97656 7.5H7.14844C7.3418 7.5 7.5 7.6582 7.5 7.85156V9.02344C7.5 9.2168 7.3418 9.375 7.14844 9.375H5.97656C5.7832 9.375 5.625 9.2168 5.625 9.02344V7.85156ZM5.625 11.6016C5.625 11.4082 5.7832 11.25 5.97656 11.25H7.14844C7.3418 11.25 7.5 11.4082 7.5 11.6016V12.7734C7.5 12.9668 7.3418 13.125 7.14844 13.125H5.97656C5.7832 13.125 5.625 12.9668 5.625 12.7734V11.6016ZM1.875 7.85156C1.875 7.6582 2.0332 7.5 2.22656 7.5H3.39844C3.5918 7.5 3.75 7.6582 3.75 7.85156V9.02344C3.75 9.2168 3.5918 9.375 3.39844 9.375H2.22656C2.0332 9.375 1.875 9.2168 1.875 9.02344V7.85156ZM1.875 11.6016C1.875 11.4082 2.0332 11.25 2.22656 11.25H3.39844C3.5918 11.25 3.75 11.4082 3.75 11.6016V12.7734C3.75 12.9668 3.5918 13.125 3.39844 13.125H2.22656C2.0332 13.125 1.875 12.9668 1.875 12.7734V11.6016ZM11.7188 1.875H10.3125V0.46875C10.3125 0.210938 10.1016 0 9.84375 0H8.90625C8.64844 0 8.4375 0.210938 8.4375 0.46875V1.875H4.6875V0.46875C4.6875 0.210938 4.47656 0 4.21875 0H3.28125C3.02344 0 2.8125 0.210938 2.8125 0.46875V1.875H1.40625C0.629883 1.875 0 2.50488 0 3.28125V4.6875H13.125V3.28125C13.125 2.50488 12.4951 1.875 11.7188 1.875Z" fill="#596263"/>
                    </svg>
                </div>
                <div class="detail_title text-[body_text]">
                    Dev. Est. Settl. Date:
                    <div class="detail text-heading"><b>{{ project_detail?.project_enddate || null }}</b></div>
                </div>
                </div>
            </div>
        </div>
        <div class="terms_info grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-x-[50px] gap-y-[20px] mb-[30px]">
            <div v-if="project_detail?.incentive" class="info_box w-full">
                <div class="info_title mb-[10px] text-heading"><b>Incentives</b></div>
                <div class="info_desc text-body_text" v-html="project_detail?.incentive"></div>
            </div>
            <div v-if="project_detail?.project_term" class="info_box  w-full">
                <div class="info_title mb-[10px] text-heading"><b>Sale Requirements</b></div>
                <div class="info_desc" v-html="project_detail?.project_term"></div>
            </div>
            <div v-if="project_detail?.important_information" class="info_box  w-full">
                <div class="info_title mb-[10px] text-heading"><b>Important Information</b></div>
                <div class="info_desc" v-html="project_detail?.important_information"></div>
            </div>
        </div>
        <!-- <div v-if="project_detail.multistage == 0" class="property_manager-details border py-[20px] px-[25px] shadow-sm rounded-[7px]">
            <div class="manager mb-[15px] text-primary"><b> Initial Property Manager</b></div>
            <div class="manager_info mb-[15px] flex gap-x-[70px] gap-y-[20px] flex-wrap">
                <div class="company text-body_text"><b class="text-heading">Company:</b> {{ project_detail?.initial_pm_company }}</div>
                <div class="term text-body_text"><b class="text-heading">Term:</b> {{ project_detail?.initial_pm_type }}</div>
                <div class="rate text-body_text"><b class="text-heading">Rate:</b> {{ project_detail?.initial_pm_term }}</div>
                <div class="rate text-body_text"><b class="text-heading">Type:</b> {{ project_detail?.initial_pm_rate }}</div>
            </div>
            <div class="manager mb-[15px] text-primary"><b>Permanent Property Manager</b></div>
            <div class="manager_info flex gap-x-[70px] gap-y-[20px] flex-wrap">
                <div class="company text-body_text"><b class="text-heading">Company:</b> {{ project_detail?.perm_pm_company }}</div>
                <div class="term text-body_text"><b class="text-heading">Term:</b> {{ project_detail?.perm_pm_type }}</div>
                <div class="rate text-body_text"><b class="text-heading">Rate:</b> {{ project_detail?.perm_pm_term }}</div>
                <div class="rate text-body_text"><b class="text-heading">Type:</b> {{ project_detail?.perm_pm_rate }}</div>
            </div>
        </div> -->
    </div>
</template>
<script>
import { Button } from 'frappe-ui'
export default {
    name: 'Details',
    componenets: {
        Button
    },
    props: {
        project_detail: Object,
        projectSummury: Object
    }
}
</script>