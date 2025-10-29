<template>
    <div id="uget" class="flex-col alitems-center large-gap top-bottom-large-padding" style=" background-color: rgba(244, 247, 251, 1);">
        <div class="flex-col alitems-center container-width large-gap">
            <div class="flex-col alitems-center" style="gap: 12px;">
                <h1>Что вы получаете</h1>
                <div style="background-color: var(--black); height: 2px; border-radius: 2px; width: 120px;"></div>
            </div>
            <div class="flex-col medium-gap" style="width: 100%;">
                <div class="mobile-wrap-column medium-gap">
                    <YouGetCard style="flex: 1;" text="Персональный бухгалтер и контроль качества старшим партнёром" />
                    <YouGetCard style="flex: 1;" text="Работаем в ваших системах: 1С, SAP, Bitrix24, Excel" />
                </div>
                <div class="mobile-wrap-column medium-gap">
                    <YouGetCard style="flex: 1;" text="Договорная ответственность и конфиденциальность" />
                    <YouGetCard style="flex: 1;" text="Онбординг за пять рабочих дней — без остановки процессов" />
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import YouGetCard from '@/components/YouGetCard.vue';
</script>