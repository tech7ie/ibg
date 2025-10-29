<template>
<div class="area-container">
  <input
    type="text"
    class="styled-area"
    :style="{backgroundColor: props.error ? 'rgba(68, 37, 78)' : 'rgba(21, 46, 82, 1)', borderColor: props.error ? 'rgba(255, 0, 64, 1)' : 'rgba(255, 0, 64, 0)'}"
    :placeholder="title"
    v-model="localValue"
  >
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps({
  modelValue: String,
  title: String,
  error: Boolean
});

const emit = defineEmits(['update:modelValue']);

const localValue = ref(props.modelValue);

watch(localValue, (newValue) => {
  emit('update:modelValue', newValue);
});
</script>

<style scoped>
.area-container {
    width: 100%;
  height: 100%;
  align-items: stretch;
}

.styled-area{
    box-sizing: border-box;
    text-align: left; /* Убедитесь, что горизонтальное выравнивание - по левому краю */
  vertical-align: top;
    font-weight: 600;
    background-color: rgba(21, 46, 82, 1);
  border-radius: 12px; /* Радиус скругления углов */
  padding: 12px; /* Внутренние отступы */
  border: 1px solid rgba(21, 46, 82, 1); /* Цвет границы */
  outline: none; /* Удаляет стандартный контур при фокусе */
  width: 100%; /* Занимает доступную ширину в контейнере */
  min-height: 120px;
  box-sizing: border-box; /* Учитывает padding и border в указанные размеры */
}

.styled-input:focus {
  background-color: rgba(27, 58, 103, 1) /* Более тёмный цвет границы при фокусе */
}

</style>
