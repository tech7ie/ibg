<script setup>
const props = defineProps({
    title: String,
    body: String,
    icon: String
})
</script>

<template>
    <div class="service-card-container flex-col alitems-start">
        <img style="height: 80px;" :src="props.icon" />
        <div class="flex-col" style="gap: 16px">
            <h2>{{ props.title }}</h2>
            <h3>{{ props.body }}</h3>
        </div>
    </div>
</template>

<style scoped>
.service-card-container {
    color: var(--black);
    background-color: rgb(0,0,0,0);
    border-radius: 24px;
    border: 1px solid rgba(213, 222, 235, 1);
    gap: 30px;
    padding: 20px;

}
</style>
