<template>
    <div class="login_page h-screen flex items-center justify-center bg-cover bg-center" style="background:linear-gradient(180deg, rgba(37, 48, 49, 0.70) 23.29%, rgba(37, 48, 49, 0.50) 100%), url('/src/assets/images/login_bg.png')">
        <div class="fw-page px-[20px] w-full">
            <div class="mx-auto">
                <div class="flex flex-col justify-center items-center gap-[85px]">
                    <div class="logo">
                        <img src="../assets/images/logo.png" alt="" class="w-56">
                    </div> 
                    <div class="login_form bg-white md:py-[40px] md:px-[30px] sm:p-[20px] p-[20px] max-w-[582px] w-full rounded-[10px] shadow-md">
                        <form>
                            <div class="form_title md:text-[30px] sm:text-[20px] text-[20px] md:mb-[40px] sm:mb-[15px] mb-[15px] font-extrabold">LOGIN</div>
                            <div class="fields_group flex flex-col md:gap-[25px] sm:gap-[20px] gap-[20px]">
                                <div class="field">
                                    <div class="mb-2"><label class="text-heading font-medium">Email or Username*</label></div>
                                    <FormControl :type="'email'" v-model="email" size="lg" variant="outline" placeholder="Enter your email address"/>
                                </div>
                                <div class="field">
                                    <div class="lablel_attch flex justify-between mb-2">
                                    <label class="text-heading font-medium">Password*</label>
                                    <label class="text-primary font-medium">Forgot Password?</label>
                                    </div>
                                    <FormControl :type="'password'" v-model="password" size="lg" variant="outline" placeholder="Password"/>
                                </div>
                                <div class="checkbox_field md:mb-[40px] sm:mb-[20px] mb-[20px]">
                                    <FormControl :type="'checkbox'" size="lg" variant="outline" label="Remember Information"/>
                                </div>
                                <div class="btn_field">
                                    <Button  variant="solid" size="lg" label="Login" v-on:click.prevent="login" class="bg-primary px-[30px]" />
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { FormControl, Button } from 'frappe-ui'
import { session } from '../data/session.js'

export default {
    name: 'Login',
    components: {
        FormControl,
        Button,
    },
    data() {
        return {
            email:"",
            password:"",
            loading:false
        }
    },
    methods: {
        login () {
            this.loading = true
            session.login.submit({
                email: this.email,
                password: this.password,
            })
        },
    },
}
</script>