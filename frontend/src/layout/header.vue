<template>
    <header class="header_navigation py-4 px-7 bg-heading">
        <div class="header_content">
            <div class="flex items-center justify-between">
                <div class="logo">
                    <router-link to="/" class=""><img src="../assets/images/logo.png" alt="" class="lg:w-56 sm:w-40 w-40"></router-link>
                </div>
                <div class="nav_bar">
                    <div class="menu lg:block sm:hidden hidden">
                        <ul class="nav flex gap-5 items-center justify-end text-white">
                            <li class="nav-item"><router-link to="/" class="">Home</router-link></li>
                            <li class="nav-item"><router-link to="/project" class="">Project</router-link></li>
                            <li class="nav-item">Priority Stock</li>
                            <li class="nav-item">
                                <Dropdown :options="options" :button="{ label: 'Account', variant: 'solid', theme:'transparent', class: 'bg-transparent hover:bg-transparent text-white p-0 d-btn'}"/>
                            </li>
                        </ul>
                    </div>
                    <div class="mobile_menu">
                        <div @click="showMenu = !showMenu" class="flex lg:hidden">
                        <button type="button" class=" text-white hover:text-white focus:outline-none focus:text-white">
                        <svg viewBox="0 0 24 24" class="w-6 h-6 fill-current">
                            <path fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"></path>
                        </svg>
                        </button>
                        </div>
                        <!-- Mobile Menu open: "block", Menu closed: "hidden" -->
                        <div :class="showMenu ? 'block' : 'hidden'" class="menu_links absolute bg-secondary inset-0 top-20 z-10">
                        <ul  class="text-center text-heading">
                        <li class="p-4"><router-link to="/" class="">Home</router-link></li>
                        <li class="p-4"><router-link to="/login" class="">Project</router-link></li>
                        <li class="p-4">Priority Stock</li>
                        <li class="p-4">
                            <Dropdown :options="options" :button="{ label: 'Account', theme:'transparent', class: 'bg-transparent hover:bg-transparent text-lg text-heading p-0', variant: 'solid'}"/>
                        </li>
                        </ul>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
</template>
<script>
import '../layout/header.css'
import { Dropdown } from 'frappe-ui'
import { session } from '../data/session.js'
export default {
    name: 'HeaderNavigation',
    components: {
        Dropdown
    },
    data(){
        return{
            showMenu: false,
            options: [
                {
                label: 'My Reservation',
                onClick: () => {this.$router.push({ name: "MyReservation" });},
                },
                {
                label: 'My Allocation',
                onClick: () => {this.$router.push({ name: "MyAllocation" });},
                },
                {
                label: 'Property EOI'
                },
                {
                label: 'Logout',
                onClick: () => {this.logout()},
                },
            ]
        }
    },
    methods: {
        logout(){
            session.logout.submit()
        }
    }
}
</script>