<script setup>
const props = defineProps({
    img: String
})
</script>

<template>
    <img :src="props.img" class="company-card"/>
</template>

<style scoped>
.company-card {
    height: 220px;
}
</style>
