<template>
    <div class="eoi_edit">
        <div class="eoi_edit_container lg:px-[70px] px-[20px] py-[30px]">
            <div class="flex gap-[10px] flex-wrap justify-between mb-[30px]">
                <div class="page_title text-[26px] font-bold">EOI Edit</div>
                <div class="action_btn flex gap-[15px]">
                    <Button variant="solid" size="lg" label="View EOI Details" theme="primary" @click="this.$router.push({ name: 'EoiDetail' })" class="bg-primary text-white px-[30px]"/>
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
            <div class="grid lg:grid-cols-5 grid-cols-1 gap-[30px]">
                <div class="lg:col-span-3">
                    <div class="buyer_detail_edit border rounded sm:p-[30px] p-[20px] max-w-[1079px] w-full mb-[30px]">
                        <div class="title text-[20px] text-primary font-semibold mb-[30px]">Purchasers Details</div>
                        <div class="flex flex-wrap gap-[20px] mb-[25px]">
                            <div class="field flex-auto">
                                <FormControl type="select" placeholder="Placeholder" label="Buying as:" :options="buying_as" @change="getPurchaserTypeOptions" v-model="selectedBuyingAs" size="lg" variant="outline"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl type="select" placeholder="Placeholder" label="Purchaser Type:" :options="purchaser_type" @change="getCompanyDetails" size="lg" variant="outline" v-model="selectedPurchaserType"/>
                            </div>
                        </div>
                        <div class="flex flex-wrap gap-[20px] mb-[25px]">
                            <div class="field flex-auto">
                                <FormControl type="select" placeholder="Placeholder" label="Is the Purchaser FIRB?: *" :options="is_firb" v-model="is_firb.value" size="lg" variant="outline"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Is the Purchaser Eligible for any Grants" label="Is the Purchaser Eligible for any Grants:"/>
                            </div>
                        </div>
                        <div class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" v-show="individual" size="lg" v-model="fullPurchaserName" variant="outline" placeholder="Purchaser Name" label="Purchaser Name to use on the Contract: *"/>
                                <FormControl :type="'text'" v-show="company" size="lg" v-model="fullCompanyName" variant="outline" placeholder="Company Name(ACN)" label="Entity Name to use on the Contract: *"/>
                                <FormControl :type="'text'" v-show="smsf" size="lg" v-model="fullsmsfName" variant="outline" placeholder="Company Name(ACN)" label="Entity Name to use on the Contract: *"/>
                                <FormControl :type="'text'" v-show="trust" size="lg" v-model="fulltrustName" variant="outline" placeholder="Company Name(ACN)" label="Entity Name to use on the Contract: *"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl type="select" placeholder="Placeholder" label="Deposit Type" :options="deposit_type" v-model="deposit_type.value" size="lg" variant="outline"/>
                            </div>
                        </div>
                        <!-- company details fields -->
                        <div v-show="company" class="title text-[20px] text-primary font-semibold mb-[30px]">Company Details</div>
                        <div v-show="company" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Company Name" label="Company Name: *" v-model="company_name"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Company ACN" label="Company ACN: *" v-model="company_acn"/>
                            </div>
                        </div>
                        <div v-show="company" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Company Address" label="Company Address: *" v-model="first_name"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Company Email Address" label="Company Email Address: *" v-model="middle_name"/>
                            </div>
                        </div>
                        <!-- SMSF details fields -->
                        <div v-show="smsf" class="title text-[20px] text-primary font-semibold mb-[30px]">SMSF Entity Details</div>
                        <div v-show="smsf" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="" label="Corporate Trustee for SMSF:"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="" label="Corporate Trustee ACN:"/>
                            </div>
                        </div>
                        <div v-show="smsf" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="" label="Corporate Trustee Address: *" v-model="first_name"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="" label="Corporate Trustee Email Address:" v-model="middle_name"/>
                            </div>
                        </div>
                        <div v-show="smsf" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="" label="SMSF Name: *"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="" label="Bare Trustee: *" v-model="bare_trustee"/>
                            </div>
                        </div>
                        <div v-show="smsf" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="" label="Bare Trustee ACN: *" v-model="bare_trustee_acn"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="" label="Bare Trust: *" v-model="bare_trust"/>
                            </div>
                        </div>
                        <!-- trust details fields -->
                        <div v-show="trust" class="title text-[20px] text-primary font-semibold mb-[30px]">Details of the Company who is acting as a trust</div>
                        <div v-show="trust" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Company Name" label="Company Name: *" v-model="trust_company_name"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Company ACN" label="Company ACN: *" v-model="trust_company_anc"/>
                            </div>
                        </div>
                        <div v-show="trust" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Company Address" label="Company Address: *" v-model="first_name"/>
                            </div>
                            <div class="field flex-auto">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Company Email Address" label="Company Email Address: *" v-model="middle_name"/>
                            </div>
                        </div>
                        <div v-show="trust" class="flex flex-wrap gap-[20px] mb-[30px]">
                            <div class="field w-1/2">
                                <FormControl :type="'text'" size="lg" variant="outline" placeholder="Trust Name" label="Trust Name: *" v-model="trust_name"/>
                            </div>
                        </div>
                        <!-- buyer and director -->
                        <div v-show="individual" class="buyer_section border rounded sm:p-[30px] p-[20px]">
                            <div v-for="(buyer, index) in buyers" :key="index" class="mb-[30px]">
                                <div class="flex gap-[10px] flex-wrap justify-between mb-[15px]">
                                    <div class="title text-[20px] text-primary font-semibold">Buyer {{ index + 1 }}</div>
                                    <Button variant="outline" size="lg" label="Remove Buyer" theme="red" v-show="index !== 0" @click="removeBuyer(index)" />
                                </div>
                                <div class="flex flex-wrap gap-[20px] mb-[30px]">
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="First Name" label="First Name:" v-model="first_name"/>
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Middle Name" label="Middle Name:" v-model="middle_name"/>
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Surname" label="Surname:" v-model="surname"/>
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="TFN" label="TFN:"/>
                                    </div>
                                </div>
                                <div class="flex flex-wrap gap-[20px] mb-[30px]">
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Residential Address" label="Residential Address:"/>
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Enter Email Address" label="Email Address:"/>
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Phone No." label="Phone No.:"/>
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Post Code" label="Post Code:"/>
                                    </div>
                                </div>
                            </div>
                            <Button variant="outline" size="lg" label="Add Buyer" theme="primary"  @click="addBuyer" class="text-primary border border-primary px-[30px]"/>
                        </div>
                        <div v-show="director" class="director_section border rounded sm:p-[30px] p-[20px]">
                            <div v-for="(buyer, index) in buyers" :key="index" class="mb-[30px]">
                                <div class="flex gap-[10px] flex-wrap justify-between mb-[15px]">
                                    <div class="title text-[20px] text-primary font-semibold">Director {{ index + 1 }}</div>
                                    <Button variant="outline" size="lg" label="Remove Director" theme="red" v-show="index !== 0" @click="removeBuyer(index)" />
                                </div>
                                <div class="flex flex-wrap gap-[20px] mb-[30px]">
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="First Name" label="First Name:" />
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Middle Name" label="Middle Name:" />
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Surname" label="Surname:"/>
                                    </div>
                                </div>
                                <div class="flex flex-wrap gap-[20px] mb-[30px]">
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Enter Email Address" label="Email Address:"/>
                                    </div>
                                    <div class="field flex-auto">
                                        <FormControl :type="'text'" size="lg" variant="outline" placeholder="Phone No." label="Phone No.:"/>
                                    </div>
                                </div>
                            </div>
                            <Button variant="outline" size="lg" label="Add Director" theme="primary"  @click="addBuyer" class="text-primary border border-primary px-[30px]"/>
                        </div>
                    </div>
                    <div class="submit-btn">
                        <Button variant="solid" size="lg" label="Submit Information" theme="primary" class="bg-primary text-white px-[30px]"/>
                    </div>
                </div>
                <div class="lg:col-span-2">
                    <div class="flex lg:flex-col md:flex-row sm:flex-col flex-col gap-[30px]">
                        <div class="solicitor_details border rounded p-[30px]">
                            <div class="title mb-[10px] text-heading font-semibold text-[20px]">SOLICITOR DETAILS</div>
                            <div class="desc text-body_text mb-[25px] text-sm">
                                <div>Do you consent to use our recommended Solicitor below?</div>
                                If not, please email your solicitor details to <span class="text-heading font-medium">admin@orbisporpertysolution.com</span>
                            </div>
                            <div class="flex flex-wrap gap-[20px] mb-[25px]">
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Solicitor" label="Solicitor:"/>
                                </div>
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Phone" label="Phone:"/>
                                </div>
                            </div>
                            <div class="flex flex-wrap gap-[20px] mb-[25px]">
                                <div class="field flex-auto">
                                    <FormControl :type="'email'" size="lg" variant="subtle" placeholder="Email" label="Email:"/>
                                </div>
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Fax" label="Fax:"/>
                                </div>
                            </div>
                            <div class="flex flex-col flex-wrap gap-[25px]">
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Address" label="Address:"/>
                                </div>
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Postal Address" label="Postal Address:"/>
                                </div>
                            </div>
                        </div>
                        <div class="broker_details border rounded p-[30px]">
                            <div class="title mb-[10px] text-heading font-semibold text-[20px]">MORTGAGE BROKER DETAILS</div>
                            <div class="desc text-body_text mb-[25px] text-sm">
                                <div>Do you consent to use our recommended Mortgage Broker below?</div>
                                If not, please email your mortgage details to <span class="text-heading font-medium">admin@orbisporpertysolution.com</span>
                            </div>
                            <div class="flex flex-wrap gap-[20px] mb-[25px]">
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Mortgage Broker Firm" label="Mortgage Broker Firm:"/>
                                </div>
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Phone" label="Phone:"/>
                                </div>
                            </div>
                            <div class="flex flex-wrap gap-[20px] mb-[25px]">
                                <div class="field flex-auto">
                                    <FormControl :type="'email'" size="lg" variant="subtle" placeholder="Email" label="Email:"/>
                                </div>
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Fax" label="Fax:"/>
                                </div>
                            </div>
                            <div class="flex flex-col flex-wrap gap-[25px]">
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Address" label="Address:"/>
                                </div>
                                <div class="field flex-auto">
                                    <FormControl :type="'text'" size="lg" variant="subtle" placeholder="Postal Address" label="Postal Address:"/>
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
    name: 'EOIedit',
    components: {
        FormControl, 
        Button
    },
    data(){
        return{
            first_name:'',
            middle_name:'',
            surname:'',
            company_name: '',
            company_acn: '',
            bare_trustee: '',
            bare_trustee_acn: '',
            bare_trust: '',
            trust_company_name:'',
            trust_company_anc:'',
            trust_name:'',
            buyers: [{}], // Initial buyer
            buying_as: [
                { label: 'Individual', value: 'individual' },
                { label: 'Company', value: 'company' },
            ],
            is_firb: [
                { label: 'Yes', value: 'yes' },
                { label: 'No', value: 'no' },
            ],
            deposit_type: [
                { label: 'Cash', value: 'cash' },
                { label: 'Personal Loan', value: 'personal_loan' },
                { label: 'Refinance', value: 'refinance' },
                { label: 'SMSF', value: 'smsf' },
            ],
            purchaser_type:[],
            selectedBuyingAs: '', // Selected Buying As option
            selectedPurchaserType: '', // Selected Purchaser Type option
            individual: true,
            company: false,
            smsf: false,
            trust: false,
            director: false,
            Status: [
                { label: 'Pending', value: 'pending' },
                { label: 'To be sent', value: 'to_be_sent' },
                { label: 'Sent', value: 'sent' },
                { label: 'Signed', value: 'signed' },
            ],
        }
    },
    computed: {
        fullPurchaserName() {
            return this.first_name + " " + this.middle_name + " " + this.surname;
        },
        fullCompanyName() {
            if(this.company_acn !== "")
                return this.company_name + " ACN " + this.company_acn;
            else return this.company_name
        },
        fullsmsfName() {
            if(this.bare_trustee_acn !== "")
            return this.bare_trustee + " ACN " + this.bare_trustee_acn;
           else if(this.bare_trust !== "")
           return this.bare_trustee +  " ATF " + this.bare_trust;
           else return this.bare_trustee
        },
        fulltrustName() {
            if(this.trust_company_anc !== "")
            return this.trust_company_name + " ACN " + this.trust_company_anc;
            else if(this.trust_name !== "")
            return this.trust_company_name + " ATF " + this.trust_name;
            else return this.trust_company_name
        },

    },
    methods: {
        addBuyer() {
        this.buyers.push({}); // Add a new buyer object to the array
        },
        removeBuyer(index) {
            this.buyers.splice(index, 1); // Remove the buyer at the specified index
        },
        getPurchaserTypeOptions() {
            if (this.selectedBuyingAs === 'individual') {
                this.individual = true
                this.purchaser_type = [
                    { label: 'Investor', value: 'investor' },
                    { label: 'Owner Occupier', value: 'owner_occupier' },
                ];
                this.selectedPurchaserType = 'investor';
            } else if (this.selectedBuyingAs === 'company') {
                this.individual = false
                this.company = true
                this.director = true
                this.purchaser_type = [
                    { label: 'Company', value: 'company' },
                    { label: 'SMSF', value: 'smsf' },
                    { label: 'Trust', value: 'trust' },
                ];
                this.selectedPurchaserType = 'company';
            } else {
                this.purchaser_type = [];
            }
        },
        getCompanyDetails(){
            if (this.selectedPurchaserType === 'company') {
                    this.company = true
                    this.smsf = false
                    this.trust = false
                } else if (this.selectedPurchaserType === 'smsf') {
                    this.company = false
                    this.smsf = true
                    this.trust = false
                }
                else if (this.selectedPurchaserType === 'trust') {
                    this.company = false
                    this.smsf = false
                    this.trust = true
                }
                console.log(this.company);
        }
    },
}
</script>