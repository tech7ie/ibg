<script setup>
import { computed } from 'vue';

const props = defineProps({
    title: String,
    transporent: {
        type: Boolean,
        default: false
    },
    blackTitle: {
        type: Boolean,
        default: false
    }
})
</script>

<template>
    <button
        class="main-button"
        :style="{
            color: props.blackTitle ? 'var(--black)' : 'white',
            backgroundColor: props.transporent ? 'rgba(0,0,0,0)' : 'var(--aqua)',
            borderColor: props.transporent ? 'white' : 'rgba(0,0,0,0)'
        }"
        :name="`button-${title}`"
    >
        {{ props.title }}
    </button>
</template>

<style scoped>
.main-button{
    display: flex;
    align-items: center;
    align-items: center;
    justify-content: center;
    padding: 12px 24px 12px 24px;
    border-radius: 8px;
    gap: 10px;
    border: 1px solid;
    cursor: pointer;

    appearance: none;
    background: none;
    margin: 0px;
}

.main-button:focus {
    outline: none;
}

.main-button:hover {
    filter: brightness(90%);
}

</style>
