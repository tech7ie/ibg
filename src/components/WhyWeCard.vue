<script setup>
const props = defineProps({
    img: String,
    title: String,
    body: String
})
</script>

<template>
    <div id="whyWee" class="why-card-container flex-col alitems-center justy-center medium-gap" style="color: white; width: 100%;">
        <img :src="props.img" class="why-img"/>
        <div class="flex-col alitems-center justy-center">
            <h2 class="why-we-title-text" style="text-align: center;">{{ title }}</h2>
            <h3 class="why-we-body-text" style="text-align: center;">{{ body }}</h3>
        </div>
    </div>
</template>

<style scoped>
.why-img {
    height: 64px;
}
.why-card-container {
    background-color: var(--black);
    border: 1px solid rgba(20, 49, 91, 1);
    border-radius: 20px;
    padding: 10px 0px 10px 0px;
}
</style>
