<template>
    <header class="flex-row alitems-center justy-center"
        style="z-index: 99; position: fixed; top: 0; width: 100%; height: 80px;background-color: rgba(0,0,0,0.3);"
    >
        <div class="flex-row alitems-center container-width">
            <RouterLink to="/">
            <img :src="LogoImg"  />
            </RouterLink>
            <div class="flex-row nav-hide medium-gap" style="margin-left: auto; padding: 4px 0px 4px 0px; justify-content: space-between; width: 50%;">
                <a href="#story">О нас</a>
                <a href="#uget">Преимущества</a>
                <a href="#news">Новости</a>
                <a href="#services">О нашей бухгалтерии</a>
            </div>
            <div style="margin-left: auto;">
                <a href="#feed">
                <Button :transporent="true" title="Оставить контакты"  class="nav-hide"/>
                </a>
                <MenuButtom @click="isOpen = !isOpen" :is-open="isOpen" class="mobile-only menu-show"/>
            </div>
            
        </div>
    </header>
    <transition name="modal-fade">
        <div v-if="isOpen" class="modal">
        <div class="modal-content">
            <a href="#">Кадровый учет</a>
            <a href="#">Налоговое планирование</a>
            <a href="#">Финансовая аналитика</a>
            <a href="#">Восстановление бухгалтерии</a>
        </div>
        </div>
  </transition>
    <!-- <div style="height: 10vh; background-color: rgba(0,0,0,1); z-index: 0;"></div> -->
</template>
<script setup>
import LogoImg from '@/assets/logo.svg'
import Button from '@/components/Button.vue';
import MenuButtom from './MenuButtom.vue';

import { ref } from 'vue';

const isOpen = ref(false)

</script>

<style scoped>
.modal {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 90vh;
  background-color: rgba(3, 14, 31, 1);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  opacity: 1;
  transition: opacity 0.3s ease;
}

.modal-content {
  display: flex;
  flex-direction: column;
  align-items: end;
  justify-content: end;
  margin-left: auto;
  margin-bottom: auto;
  margin: 50px 50px auto auto;
}

.modal-content a {
  margin: 10px 0;
  color: white;
  text-decoration: none;
  font-size: 20px;
}

.modal-content a:hover {
  text-decoration: underline;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.3s ease;
}

.modal-fade-enter, .modal-fade-leave-to {
  opacity: 0;
}
@media (max-width: 1519px) {
    .nav-hide{
      display: none;
    }
    .menu-show {
      display: flex;
    }
}
</style>