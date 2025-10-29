<template>
    <div id="feed" class="flex-row alitems-center justy-center top-bottom-large-padding" style="background-color: var(--black); color: white;">
        <div class="flex-col container-width  large-gap">
            <div class="flex-col medium-gap">
                <h1>Оставьте свои контактные данные</h1>
                <h3>И мы вернёмся к вам в течение рабочего дня</h3>
            </div>
            <form class="mobile-wrap-column container-width  medium-gap" @submit.prevent="handleSubmit">
                <div class="flex-col container-width  medium-gap ">
                    <div class="mobile-wrap-column medium-gap">
                        <Input v-model="formData.fio" title="Важи Фамилия и Имя"/>
                        <Input v-model="formData.number" title="Телефон"/>
                    </div>
                    <div class="mobile-wrap-column medium-gap">
                        <Input v-model="formData.company" title="Назвиние вашей компании"/>
                        <Input :error="error" v-model="formData.email" title="Электронная почта*"/>
                    </div>
                </div>
                <Textarea v-model="formData.text" title="Кратко опишите задачу" />
            </form>
                <div class="mobile-wrap-column-reverse alitems-center large-gap" >
                    <Button @click="handleSubmit" title="Отправить" class="mobile-width" />
                    <a>Нажимая на кнопку “Отправить”, Вы соглашаетесь с Пользовательским соглашением и Политикой конфиденциальности</a>
                </div>
        </div>
    </div>
</template>
<script setup>
import Button from '@/components/Button.vue';
import Input from '@/components/Input.vue';
import Textarea from '@/components/Textarea.vue';
import { reactive, ref } from 'vue';

const error = ref(false)
const formData = reactive({
  email: '',
  fio: '',
  number: '',
  company: '',
  text: ''
});

function handleSubmit() {
    if (formData.email == '') {error.value = true}
    else{
        error.value = false
  alert(`Данные отправлены: Email - ${formData}`);}
}
</script>