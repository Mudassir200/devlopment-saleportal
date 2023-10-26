<template>
    <div class="eoi_detail">
        <div class="eoi_detail-container lg:px-[70px] px-[20px] py-[30px]">
            <div class="flex gap-[10px] flex-wrap justify-between mb-[30px]">
                <div class="page_title text-[26px] font-bold ">EOI Details</div>
                <div class="action_btns flex gap-[15px]">
                    <Button variant="solid" size="lg" label="Edit EOI" theme="secondary" @click="this.$router.push({ name: 'EOIedit' })" class="bg-secondary text-heading px-[30px]"/>
                    <Button variant="solid" size="lg" label="Generate PDF" theme="primary" class="bg-primary text-white px-[30px]"/>
                </div>
            </div>
            <div class="agent_property_details flex flex-wrap gap-x-[60px] gap-y-[30px] sm:p-[30px] p-[20px] border rounded mb-[30px]">
                <div class="agent_details">
                    <div class="title font-semibold mb-[20px]">AGENT DETAILS</div>
                    <div class="details">
                        <ul>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>Name:</b> <p>Century Estate</p></li>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>Address:</b> <p>Three International Towers, Level 24, 300 Barangaroo Avenue, NSW</p></li>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>Phone:</b> <p>1300 766 791</p></li>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>Email:</b> <p>admin@orbisporpertysolution.com</p></li>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>ABN:</b> <p>17602514670</p></li>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>Postcode:</b> <p>2137</p></li>
                        </ul>
                    </div>
                </div>
                <div class="property_details">
                    <div class="title font-semibold mb-[20px]">PROPERTY DETAILS</div>
                    <div class="details flex gap-[20px]">
                        <ul>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>Project & Estate:</b> <p>Century Estate</p></li>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>Land Price:</b> <p>225000</p></li>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>House Price:</b> <p>269500</p></li>
                            <li class="mb-[15px] flex flex-wrap gap-x-[20px] gap-y-[5px]"><b>Lot No:</b> <p>823</p></li>
                        </ul>
                    </div>
                    <div class="total_price flex gap-[40px] font-semibold text-[20px]">
                        <div>Total Price:</div>
                        <div>494500</div>
                    </div>
                </div>
                <div class="upgrades max-w-[518px] w-full">
                    <div class="title font-semibold mb-[20px] text-[18px]">Upgrades/Colour Schemes </div>
                    <div class="text-body_text mb-[10px]">10 Year 3.5% RG PLUS 5 Year Price Guarantee PLUS 20 Years</div>
                    <div class="text-body_text mb-[10px]">Structure Guarantee.</div>
                    <div class="text-body_text mb-[10px]">$10k rebate on the build.</div>
                    <div class="text-body_text mb-[10px]">If contracts are signed with full deposit (10% land and 5% build) within 14 days of EOI get 10% interest paid on Deposit (Deposit is $42,000 over 1 year = $4,200)</div>
                </div>
            </div>
            <div class="other_details">
                <div class="grid lg:grid-cols-5 grid-cols-1 gap-[30px]">
                    <div class="lg:col-span-3 buyer_details_and_eoi_history">
                        <div class="buyer_details border rounded sm:p-[30px] p-[20px] max-w-[1079px] w-full mb-[30px]">
                            <div class="title text-[20px] text-primary font-semibold mb-[30px]">Purchasers Details</div>
                            <div class="grid xl:grid-cols-3 lg:grid-cols-1 sm:grid-cols-2 grid-cols-1 gap-[25px] mb-[25px] justify-between">
                                <div class="purchaser_type">
                                    <div class="text-body_text">Purchaser Type:</div>
                                    <div class="text-heading font-medium">Trust</div>
                                </div>
                                <div class="purchaser_type">
                                    <div class="text-body_text">Is the Purchaser FIRB?</div>
                                    <div class="text-heading font-medium">Yes</div>
                                </div>
                                <div class="purchaser_type">
                                    <div class="text-body_text">Is the Purchaser Eligible for any Grants:</div>
                                    <div class="text-heading font-medium">No</div>
                                </div>
                                <div class="purchaser_type">
                                    <div class="text-body_text">Entity Name:</div>
                                    <div class="text-heading font-medium">Dream House</div>
                                </div>
                                <div class="purchaser_type">
                                    <div class="text-body_text">Contact Person:</div>
                                    <div class="text-heading font-medium">John Hendry Smith</div>
                                </div>
                            </div>
                            <div class="title text-[20px] text-primary font-semibold mb-[15px]">Buyer 1</div>
                            <div class="buyer sm:p-[20px] p-[15px] border rounded mb-[30px]">
                                <div class="grid xl:grid-cols-3 lg:grid-cols-1 md:grid-cols-2 gap-[25px] pb-[20px] mb-[20px] border-b">
                                        <div class="name flex flex-wrap gap-[15px]">
                                            <div class="label text-body_text">Name:</div>
                                            <div class="text-heading font-medium">John Stephen Donald</div>
                                        </div>
                                        <div class="phone flex flex-wrap gap-[15px]">
                                            <div class="label text-body_text">Phone No.:</div>
                                            <div class="text-heading font-medium">+1 234 5678 900</div>
                                        </div>
                                        <div class="name flex flex-wrap gap-[15px]">
                                            <div class="label text-body_text">Email:</div>
                                            <div class="text-heading font-medium">john@gmail.com</div>
                                        </div>
                                        <div class="name flex flex-wrap gap-[15px] w-2/6">
                                            <div class="label text-body_text">TFN:</div>
                                            <div class="text-heading font-medium">1234</div>
                                        </div>
                                        <div class="name flex flex-wrap gap-[15px]">
                                            <div class="label text-body_text">Address:</div>
                                            <div class="text-heading font-medium">Los Angeles, CA</div>
                                        </div>
                                </div>
                                <div class="flex flex-wrap items-center justify-between gap-[20px]">
                                    <div class="flex flex-wrap gap-[30px]">
                                        <div class="text-body_text md:text-lg text-sm">status: <span class="text-white text-sm px-[12px] py-[3px] bg-[#19B674] rounded-full">Submit</span></div>
                                        <div class="text-body_text md:text-lg text-sm">Last Updated: September 30, 2023</div>
                                    </div>
                                    <div class="action_btns flex flex-wrap gap-[15px]">
                                        <Button variant="solid" size="lg" label="Download PDF" theme="secondary" class="bg-secondary text-heading px-[30px]"/>
                                        <Button variant="solid" size="lg" label="Send for Sign" theme="primary" class="bg-primary text-white px-[30pxpx]"/>
                                    </div>
                                </div>
                            </div>
                            <div class="title text-[20px] text-primary font-semibold mb-[15px]">Buyer 2</div>
                            <div class="buyer p-[20px] border rounded mb-[30px]">
                                <div class="grid xl:grid-cols-3 lg:grid-cols-1 md:grid-cols-2 gap-[25px] pb-[20px] mb-[20px] border-b">
                                        <div class="name flex gap-[15px]">
                                            <div class="label text-body_text">Name:</div>
                                            <div class="text-heading font-medium">James Jhonson</div>
                                        </div>
                                        <div class="phone flex gap-[15px]">
                                            <div class="label text-body_text">Phone No.:</div>
                                            <div class="text-heading font-medium">+1 234 5678 900</div>
                                        </div>
                                        <div class="name flex gap-[15px]">
                                            <div class="label text-body_text">Email:</div>
                                            <div class="text-heading font-medium">James@gmail.com</div>
                                        </div>
                                        <div class="name flex gap-[15px]">
                                            <div class="label text-body_text">TFN:</div>
                                            <div class="text-heading font-medium">1234</div>
                                        </div>
                                        <div class="name flex gap-[15px]">
                                            <div class="label text-body_text">Address:</div>
                                            <div class="text-heading font-medium">Los Angeles, CA</div>
                                        </div>
                                </div>
                                <div class="flex flex-wrap items-center justify-between gap-[20px]">
                                    <div class="flex flex-wrap gap-[30px]">
                                        <div class="text-body_text md:text-lg text-sm">status: <span class="text-white text-sm px-[12px] py-[3px] bg-[#ED7F19] rounded-full">Pending</span></div>
                                        <div class="text-body_text md:text-lg text-sm">Last Updated: September 30, 2023</div>
                                    </div>
                                    <div class="action_btns flex flex-wrap gap-[15px]">
                                        <Button variant="solid" size="lg" label="Download PDF" theme="secondary" class="bg-secondary text-heading px-[30px]"/>
                                        <Button variant="solid" size="lg" label="Send for Sign" theme="primary" class="bg-primary text-white px-[30pxpx]"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="eoi_history border rounded p-[30px] overflow-auto">
                            <div class="title text-heading text-[20px] font-semibold mb-[20px]">EOI HISTORY</div>
                            <div class="table w-full mb-[30px]">
                                <table class="text-left text-sm font-light w-full border">
                                    <thead class="font-medium text-[16px] text-heading">
                                        <tr>
                                            <th v-for="(column, index) in historyTable_column" :key="index" class="px-4 py-4 border">{{ column.title }}</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="(item, rowIndex) in historyTable_data" :key="rowIndex">
                                            <td v-for="(column, colIndex) in historyTable_column" :key="colIndex" class="px-4 py-4 font-normal border">
                                                <span :class="{
                                                                'text-[#19B674] font-medium': item[column.value] === 'Signed',
                                                                'text-[#0078B9] font-medium': item[column.value] === 'Sent',
                                                                'text-[#ED7F19] font-medium': item[column.value] === 'To be Sent'
                                                                }">
                                                                {{ item[column.value] }}
                                                            </span>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div class="add_history">
                                <div class="title text-heading text-[20px] font-semibold mb-[20px]">ADD EOI HISTORY</div>
                                <div class="flex gap-[15px] items-end flex-wrap">
                                    <div class="field flex-auto">
                                    <FormControl type="select" placeholder="Placeholder" label="Search By:" :options="Status" size="lg" variant="subtle"/>
                                    </div>
                                    <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Add Comment" :disabled="false" label="Comment:"/>
                                    </div>
                                    <div class="field">
                                        <Button variant="solid" size="lg" label="Add Status" theme="primary" class="bg-primary text-white px-[30px]"/>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="lg:col-span-2 solicitor_broker_details">
                        <div class="solicitor_details border rounded p-[30px] mb-[30px]">
                            <div class="title mb-[30px] text-heading font-bold text-[20px]">Solicitor Details</div>
                            <div class="grid xl:grid-cols-3 lg:grid-cols-1 md:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-[25px] mb-[25px]">
                                <div class="name">
                                    <div class="text-body_text">Solicitor:</div>
                                    <div class="text-heading font-medium">Michael Canterbury</div>
                                </div>
                                <div class="phone">
                                    <div class="text-body_text">Phone:</div>
                                    <div class="text-heading font-medium">+1 2345 678 900</div>
                                </div>
                                <div class="email">
                                    <div class="text-body_text">Email:</div>
                                    <div class="text-heading font-medium">michael@gmail.com</div>
                                </div>
                                <div class="contact">
                                    <div class="text-body_text">contact:</div>
                                    <div class="text-heading font-medium">0123 456 789</div>
                                </div>
                                <div class="post_address">
                                    <div class="text-body_text">Postal Address:</div>
                                    <div class="text-heading font-medium">Century Estate, Main Road.</div>
                                </div>
                                <div class="fax">
                                    <div class="text-body_text">Fax:</div>
                                    <div class="text-heading font-medium">9876 5432</div>
                                </div>
                                <div class="address">
                                    <div class="text-body_text">Address:</div>
                                    <div class="text-heading font-medium">Century Estate, CA.</div>
                                </div>
                            </div>
                        </div>
                        <div class="broker_details border rounded p-[30px]">
                            <div class="title mb-[30px] text-heading font-bold text-[20px]">Mortgage Broker Details</div>
                            <div class="grid xl:grid-cols-3 lg:grid-cols-1 md:grid-cols-3 sm:grid-cols-2 grid-cols-1 mb-[25px] gap-[25px]">
                                <div class="name">
                                    <div class="text-body_text">Mortgage Broker Firm:</div>
                                    <div class="text-heading font-medium">Dream House</div>
                                </div>
                                <div class="phone">
                                    <div class="text-body_text">Phone:</div>
                                    <div class="text-heading font-medium">+1 2345 678 900</div>
                                </div>
                                <div class="email">
                                    <div class="text-body_text">Email:</div>
                                    <div class="text-heading font-medium">michael@gmail.com</div>
                                </div>
                                <div class="contact">
                                    <div class="text-body_text">Broker:</div>
                                    <div class="text-heading font-medium">Dave Lundine</div>
                                </div>
                                <div class="fax">
                                    <div class="text-body_text">Fax:</div>
                                    <div class="text-heading font-medium">9876 5432</div>
                                </div>
                                <div class="address">
                                    <div class="text-body_text">Address:</div>
                                    <div class="text-heading font-medium">Century Estate, CA.</div>
                                </div>
                                <div class="post_address">
                                    <div class="text-body_text">Postal Address:</div>
                                    <div class="text-heading font-medium">Century Estate, Main Road.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { FormControl, Button} from 'frappe-ui'
export default {
    name: 'EoiDetail',
    components: {
        FormControl,
        Button
    },
    data(){
        return{
            Status: [
                { label: 'Pending', value: 'pending' },
                { label: 'To be sent', value: 'to_be_sent' },
                { label: 'Sent', value: 'sent' },
                { label: 'Signed', value: 'signed' },
            ],
            historyTable_column: [
                {
                    title: "Status",
                    value: "Status" 
                },
                {
                    title: "Comment",
                    value: "Comment" 
                },
                {
                    title: "Date",
                    value: "Date" 
                },
            ],
            historyTable_data:[
                { 
                    Status:"Sent", 
                    Comment:"EOI is Signed by members", 
                    Date:"19-09-2023 06:09:48"
                },
            ]
        }
    },
}
</script>