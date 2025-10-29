<template>
    <div class="flex-col alitems-center top-bottom-large-padding" style="background-color: var(--black);">
        <div class="flex-col alitems-center container-width large-gap">
            <div class="flex-col alitems-center" style="gap: 12px;">
                <h1 style="color: white;">Почему мы</h1>
                <div style="background-color: aqua; height: 2px; border-radius: 2px; width: 120px;"></div>
            </div>
            <div class="flex-row alitems-center wrap-why-cards-mobile hide-why medium-gap" style="width: 100%;">
                <WhyWeCard style="flex: 1;" :img="whyDiamond" title="Более 1000" body="клиентов" />
                <WhyWeCard style="flex: 1;" :img="Ckeckmark" title="8 лет опыта" body="на рынке" />
                <WhyWeCard style="flex: 1;" :img="People" title="Более 90" body="сотрудников" />
                <WhyWeCard style="flex: 1;" :img="Location" title="12 стран" body="мира" />
            </div>
            <div class="mobile-wrap-column alitems-center show-why medium-gap" style="width: 100%;">
                <div class="wrap-why-cards-mobile flex-col alitems-center medium-gap" style="width: 100%;">
                    <WhyWeCard style="flex: 1;" :img="whyDiamond" title="Более 1000" body="клиентов" />
                    <WhyWeCard style="flex: 1;" :img="Ckeckmark" title="8 лет опыта" body="на рынке" />
                </div>
                <div class="wrap-why-cards-mobile flex-col alitems-center medium-gap" style="width: 100%;">
                  <WhyWeCard style="flex: 1;" :img="People" title="Более 90" body="сотрудников" />
                 <WhyWeCard style="flex: 1;" :img="Location" title="12 стран" body="мира" />
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import WhyWeCard from '@/components/WhyWeCard.vue';
import whyDiamond from '@/assets/whyDiamond.svg'
import Location from '@/assets/location.svg'
import People from '@/assets/people.svg'
import Ckeckmark from '@/assets/ckeckmark.svg'
</script>

<style scoped>
@media only screen and (max-width: 550px) {
    .wrap-why-cards-mobile {
        display: flex;
        flex-direction: column;
    }
}
@media only screen and (max-width: 1250px) {
    .hide-why {
        display: none;
    }
    .show-why {
        display: flex;
    }
}
@media only screen and (min-width: 1250px) {
    .hide-why {
        display: flex;
    }
    .show-why {
        display: none;
    }
}
</style>