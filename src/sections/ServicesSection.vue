<template>
    <div id="services" class="flex-row justy-center alitems-center top-bottom-large-padding">
        <div class="flex-col alitems-center container-width large-gap">
            <div class="flex-col" style="gap: 12px; margin-right: auto;">
                <img class="crown-text-margin" :src="BaseServices" style="height: calc(6px + 3vh);" />
                <h1 class="text-align-mobile">Бухгалтерия, которой можно доверять</h1>
            </div>
            <div class="flex-col medium-gap">
                <div class="mobile-wrap-column medium-gap" style="word-wrap: break-word;">
                    <ServiceCard style="flex: 1;" title="Ведение бухучёта" body="Первичка, учёт доходов и расходов, закрытие периода, отчётность по стандартам вашей юрисдикции." :icon="iconMedal"></ServiceCard>
                    <ServiceCard style="flex: 1;" title="Расчётность" body="Расчёт налогов, подача деклараций, сверки с налоговыми органами, сопровождение камеральных и налоговых проверок." :icon="BilImg"></ServiceCard>
                    <ServiceCard style="flex: 1;" title="Зарплата и кадры" body="Расчёт заработной платы, отпусков, больничных; кадровое делопроизводство и отчётность." :icon="Humans"></ServiceCard>
                    </div>
                    <div class="mobile-wrap-column medium-gap" style="word-wrap: break-word;">
                    <ServiceCard style="flex: 1;" title="Внутренний аудит" body="Проверка данных и процессов, рекомендации по снижению рисков, подготовка к внешнему аудиту." :icon="Search"></ServiceCard>
                    <ServiceCard style="flex: 1;" title="Консалтинг и учёт" body="Диагностика, регламенты, переход на аутсорс, построение учётной политики и контрольные процедуры." :icon="Dash"></ServiceCard>
                    <ServiceCard style="flex: 1;" title="Автоматизация" body="Внедрение и поддержка 1С, интеграции с CRM/банками, сквозная аналитика." :icon="Auto"></ServiceCard>
                </div>
            </div>
            <!-- <Button title="Отправить" style="width: 100%;" class="mobile-only mobile-width" /> -->
        </div>
    </div>
</template>
<script setup>
import ServiceCard from '@/components/ServiceCard.vue';
import BaseServices from '@/assets/bestServices.svg'
import iconMedal from '@/assets/medal.svg'
import BilImg from '@/assets/bil.svg'
import Humans from '@/assets/humans.svg'
import Search from '@/assets/search.svg'
import Auto from '@/assets/auto.svg'
import Dash from '@/assets/dash.svg'
import Button from '@/components/Button.vue';
</script>

<style scoped>
@media only screen and (max-width: 550px) {
    .crown-text-margin {
        margin-right: 0;
    }
}

@media only screen and (min-width: 550px) {
    .crown-text-margin {
        margin-right: auto;
    }
}
</style>