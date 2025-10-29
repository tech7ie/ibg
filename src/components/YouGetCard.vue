<script setup>
const props = defineProps({
    text: String
})
</script>

<template>
    <div class="you-get-container flex-row medium-gap">
        <div class="flex-row alitems-center medium-gap">
            <div class="green-dot"></div>
            <h4 class="you-get-card-text">{{ text }}</h4>
        </div>
    </div>
</template>

<style scoped>
.green-dot{
    max-height: 8px;
    max-width: 8px;
    min-height: 8px;
    min-width: 8px;
    border-radius: 3px;
    background-color: var(--green);
}
.you-get-container {
    padding: 20px;
    border-radius: 12px;
    background-color: var(--gray);
    flex-wrap: wrap;
}
</style>
