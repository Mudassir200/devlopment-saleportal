<template>
    <div class="my_reservation">
        <div class="reservation_container py-[30px] lg:px-[70px] md:px-[50px] sm:px-[30px] px-[20px]">
            <div class="page_title text-[22px] font-medium mb-[20px]">My Reservation</div>
            <div class="flex flex-wrap gap-[20px] items-end mb-[30px]">
                <div class="field flex-auto">
                    <FormControl type="date" size="lg" variant="outline" placeholder="Select Date"
                        label="Reservation Date" />
                </div>
                <div class="field flex-auto">
                    <FormControl type="select" size="lg" variant="outline" :options="projects" label="Select Project" />
                </div>
                <div class="field">
                    <FormControl type="select" size="lg" variant="outline" :options="projects" label="Strategist" />
                </div>
                <div class="field">
                    <FormControl type="select" size="lg" variant="outline" :options="projects" label="Buyer Type" />
                </div>
                <div class="field">
                    <FormControl type="select" size="lg" variant="outline" :options="projects" label="Deposit Type" />
                </div>
                <div class="field">
                    <FormControl type="select" size="lg" variant="outline" :options="projects" label="Reservation Status" />
                </div>
                <div class="field">
                    <Button variant="solid" size="lg" label="Apply Filter" theme="primary"
                        class="bg-primary text-white px-[25px]" />
                </div>
            </div>
            <div class="stages_table-container max-w-[1780px] m-auto py-[30px] rounded-[10px] bg-[#F6F7F8] mb-[30px]">
                <div class="flex gap-[10px] items-center justify-between px-[30px] mb-[20px]">
                    <div class="flex gap-[10px] items-center">
                        <div>Show</div>
                        <FormControl type="select" size="lg" variant="outline" :options="Showdata" />
                        <div>Entries</div>
                    </div>
                    <FormControl :type="'search'" size="md" variant="outline" placeholder="Search.." />
                </div>
                <DataTable :tableData="stagestableData" :tableColumns="stagestableColumns" :perpageData="4" />
                <Dialog v-model="dialog2" class="text-center">
                    <template #body-title>
                        <h3>Withdrawal Confirmation</h3>
                    </template>
                    <template #body-content>
                        <p>Are you certain about withdrawing this property? If yes, please click the 'Withdraw' button below. If not, click the 'Cancel' button to retain your reservation.</p>
                    </template>
                    <template #actions>
                        <Button variant="solid" size="lg" theme="red" @click="WithdrawConfirm" class="px-[30px]">
                            Withdraw Now
                        </Button>
                        <Button class="ml-2" size="lg" @click="dialog2 = false">
                            Cancel
                        </Button>
                    </template>
                </Dialog>
            </div>
            <div v-show="success" class="confirm_text bg-[#CBEFE0] rounded-[20px] max-w-fit text-[#00AC47] py-[10px] px-[20px]">Success: Your property reservation has been withdrawn successfully.</div>
        </div>
    </div>
</template>
<script>
import {Dialog, FormControl, Button } from 'frappe-ui'
import DataTable from '../components/Data-table.vue'
export default {
    name: 'MyReservation',
    components: {
        FormControl,
        Button,
        DataTable,
        Dialog
    },
    data() {
        return {
            dialog2: false,
            success: false,
            projects: [
                { label: 'Century Estate - 15A', value: '' },
                { label: 'project 2', value: 'one_part' },
                { label: 'project 3', value: 'two_part' },
            ],
            Showdata: [
                { label: 10, value: '' },
                { label: 25, value: 25 },
                { label: 50, value: 50 },
            ],
            stagestableColumns: [
                {
                    title: 'Project Name',
                    value: 'project_name',
                    sort: true
                },
                {
                    title: 'Lot No.',
                    value: 'lot_no',
                    sort: true
                },
                {
                    title: 'Strategist',
                    value: 'strategist',
                    sort: true
                },
                {
                    title: 'Buyer Type',
                    value: 'buyer_type',
                    sort: true
                },
                {
                    title: 'Member',
                    value: 'member',
                    sort: true
                },
                {
                    title: 'Deposit Type',
                    value: 'deposit_type',
                    sort: true
                },
                {
                    title: 'Res. Date',
                    value: 'res_date',
                    sort: true
                },
                {
                    title: 'Res. Exp. Date',
                    value: 'res_exp_date',
                    sort: true
                },
                {
                    title: 'Last Status Date',
                    value: 'last_status_date',
                    sort: true
                },
                {
                    title: 'Reservation Status',
                    value: 'badge',
                    sort: true
                },
                {
                    title: 'Action',
                    value: 'action',
                    sort: false
                },
                // Add other columns as needed
            ],
            stagestableData: [
                // Add more data rows as needed
            ],
        }
    },
    methods: {
        getdata() {
            const res = [
                {
                    project_name: 'Century Estate',
                    lot_no: 'A15',
                    strategist: 'James Smith',
                    buyer_type: 'Investor',
                    member: 'Michael Jordan (1234567)',
                    deposit_type: 'Personal Loan',
                    res_date: '02-Oct-2023',
                    res_exp_date: '07-Oct-2023',
                    last_status_date: '04-Oct-2023',
                    reservation_status: "EOI Prepared"
                }
            ];
            this.stagestableData = res.map((item) => {
                let myitem = { ...item }
                if (myitem.reservation_status == 'Reserved') {
                    myitem.badge = '<div class="text-heading font-medium bg-[#DCE7E8] px-[15px] py-[7px] rounded-full">Reserved</div>';
                    myitem.action = [
                        {
                            class: "bg-[#EA4335] rounded-[5px] text-white py-[7px] px-[12px] ",
                            html: 'Withdraw',
                            action: () => {this.dialog2 = true}
                        },
                        {
                            class: "bg-[#0078B9] rounded-[5px] text-white py-[7px] px-[12px]",
                            html: "Prepare EOI",
                        }
                    ]
                } else if (myitem.reservation_status == 'EOI Prepared') {
                    myitem.badge = '<div class="text-[#076FA8] font-medium bg-[#C3E2F3] px-[15px] py-[7px] rounded-full">EOI Prepared</div>';
                    myitem.action = [
                        {
                            class: "bg-[#EA4335] rounded-[5px] text-white py-[7px] px-[12px] ",
                            html: 'Withdraw',
                            action: () => {this.dialog2 = true}
                        },
                        {
                            class: "bg-primary rounded-[5px] text-white py-[7px] px-[12px]",
                            html: "View EOI",
                            action: () => {
                                this.$router.push({ name: "EoiDetail" });
                            }
                        }
                    ]
                } else if (myitem.reservation_status == 'EOI Signed') {
                    myitem.badge = '<div class="text-[#0DAD6A] font-medium bg-[#CBEFE0] px-[15px] py-[7px] rounded-full">EOI Signed</div>';
                    myitem.action = [
                        {
                            class: "bg-primary rounded-[5px] text-white py-[7px] px-[12px]",
                            html: "View EOI",
                            action: () => {
                                this.$router.push({ name: "EoiDetail" });
                            }
                        }
                    ]
                } else if (myitem.reservation_status == 'Expired') {
                    myitem.badge = '<div class="text-[#D86E0D] font-medium bg-[#F2DCC8] px-[15px] py-[7px] rounded-full">Expired</div>';
                    myitem.action = [
                        {
                            class: "bg-primary rounded-[5px] text-white py-[7px] px-[12px]",
                            html: "View EOI",
                            action: () => {
                                this.$router.push({ name: "EoiDetail" });
                            }
                        }
                    ]
                }
                return myitem
            })
        },
        WithdrawConfirm(){
            this.dialog2 = false
            this.success = true
        }
    },
    mounted() {
        this.getdata();
    }
}
</script>