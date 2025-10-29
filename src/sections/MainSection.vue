<template>
    <div class="flex-row alitems-center justy-center" style="width: 100%; height: 100%; color: white; background: radial-gradient(circle at left bottom, rgba(7, 37, 80, 1), rgba(43, 112, 212, 0) 150%),
                        radial-gradient(circle at right bottom, rgba(14, 74, 160, 1), rgba(40, 112, 212, 0.8) 150%), radial-gradient(circle at right bottom, rgba(14, 74, 160, 1), rgba(40, 112, 212, 1) 150%);">
        <div class="flex-row alitems-center justy-center container-width" style=" height: 100vh;">
            <div class="flex-col main-text-center medium-gap" style="max-width: 740px; margin-right: auto;">
                <div class="flex-row alitems-center ">
                    <img :src="CrownImg" />
                    <h4 >Аутсорсинговая бухгалтерия</h4>
                </div>
                <h1 class="main-title" style="width: 80%;">«Вы делаете бизнес, мы ведем вашу бухгалтерию</h1>
                <h4 class="main-text-center" style="word-wrap: break-word; max-width: 600px;">Передайте нам учёт, отчётность и зарплатные проекты — освободите время для роста. Работаем прозрачно по SLA, фиксируем риски, общаемся человеческим языком.</h4>
                <div class="flex-row alitems-center justyfy-start large-gap">
                    <a href="#feed">
                    <Button title="Оставить контакты" :black-title="true"  />
                    </a>
                    <a style="color: rgba(98, 136, 194, 1);" href="#story">О компании</a>
                </div>
            </div>
            <img :src="WomanImg" class="woman-hide" style=" height: 90vh; margin-top: auto; margin-left: auto;"/>
        </div>
    </div>
</template>
<script setup>
import WomanImg from '@/assets/woman.png'
import CrownImg from '@/assets/crown.svg'
import Button from '@/components/Button.vue';
</script>

<style scoped>
@media (max-width: 1519px) {
    .woman-hide {
        display: none;
    }
    .main-text-center {
        text-align: center;
        margin-right: 0 !important;
        align-items: center;
    }
}
@media only screen and (min-height: 1200px) {
.main-title {
    font-weight: 700;
    font-size: 86px !important;
    line-height: 86px;
    min-width: 1000px;
}
    .main-text-center {
        font-weight: 400;
        font-size: 38px !important;
        line-height: 38px !important;
        min-width: 1000px;
    }
}
</style>