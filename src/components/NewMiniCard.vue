

<template>
    <div class="flex-row alitems-center" style="cursor: pointer; gap: 24px;">
        <img :src="props.icon" class="news-mini-img" />
        <div class="flex-col medium-padding new-content" style="gap: 24px; width: 200px;">
            <h3 style="font-weight: 700; font-size: 18px; inline-size: 24px; width: 100%;">{{ props.title }}</h3>
            <h4>{{ props.created_at }}</h4>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    title: String,
    created_at: String,
    icon: String
})
</script>

<style scoped>
.news-mini-img {
    object-fit: cover;
    height: 128px;
    width: 128px;
    border-radius: 8px;

}
</style>
