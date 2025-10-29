<template>
    <div id="story" class="flex-row justy-center alitems-center large-gap top-bottom-large-padding">
        <div class="flex-row alitems-center container-width story-content-adaptive medium-gap">
            <div class="flex-col text-align-mobile mobile-items-center large-gap" style=" max-width: 800px; margin-right: auto;">
                <h1>Краткая история компании</h1>
                <h3>Мы начали как небольшая команда бухгалтеров‑практиков, которые устали от «бумажной» рутины. С самого старта делали ставку на технологии, прозрачные процессы и человеческую коммуникацию. Сегодня IB Service Group — это полноценный аутсорсинговый департамент для компаний малого и среднего бизнеса в разных странах. Мы соединяем экспертизу с автоматизацией: настраиваем процессы, берём на себя ответственность за сроки и качество, и говорим на языке владельцев и руководителей.</h3>
                <Button title="Связаться с нами" />
            </div>
            <div >
                <img :src="OfficeImg" style="margin-left: auto;" class="office-img" />
            </div>
        </div>
    </div>
</template>
<script setup>
import OfficeImg from '@/assets/office.png'
import Button from '@/components/Button.vue';
</script>

<style scoped>
.office-img {
    height: calc(25vh + 200px); max-height: 500px; min-height: 300px; 
}
@media (max-width: 950px) {
    .story-content-adaptive {
        flex-direction: column-reverse;
    }
    .office-img {
        width: 100%;
        min-width: 260px;
        height: auto;
        min-height: auto;
        max-height: none;
    }
}
</style>