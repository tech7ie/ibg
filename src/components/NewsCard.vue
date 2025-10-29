<script setup>
const props = defineProps({
    title: String,
    body: String,
    icon: String
})
</script>

<template>
    <div class="new-card-container flex-col alitems-center" style="cursor: pointer;">
        <img :src="props.icon" class="news-img" />
        <div class="flex-col medium-padding new-content">
            <h4 style="font-weight: 700;">{{ props.title }}</h4>
            <h3>{{ props.body.slice(0, 100) }}...</h3>
            <a style="color: rgba(98, 136, 194, 1); margin-left: auto; margin-top: auto;" >Читать дальше</a>
        </div>
    </div>
</template>

<style scoped>
.new-card-container {
    min-width: 320px;
    max-width: 466px;
    color: var(--black);
    background-color: rgb(0,0,0,0);
    border-radius: 24px;
    border: 1px solid rgba(213, 222, 235, 1);
}
@media only screen and (min-height: 1200px) {
    .new-card-container {
    max-width: 486px;
}
    
}
.news-img {

    width: 100%;
    height: 250px;
    border-radius: 24px 24px 0px 0px;
    object-fit: cover; /* Обеспечивает покрытие и обрезку изображения */
    object-position: center; /* Центрирует изображение в контейнере */
}
.new-content {
    min-height: 200px;
    width: 90%;
    gap: 16px;
}
</style>
