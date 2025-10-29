<template>
    <div class="flex-col alitems-center" style="width: 100%; margin-top: 120px; margin-bottom: 150px;">
        <div class="flex-row container-width">
            <div v-if="currentNews" class="flex-col large-gap" style="flex: 3">
                <h1>{{ currentNews?.title }}</h1>
                <div class="flex-row alitems-center" style="gap: 8px;">
                    <img :src="DateIcon" />
                    <h4>{{ currentNews?.created_at.split('T')[0] }}</h4>
                </div>
                <!-- <img :src="currentNews?.image" v-if="currentNews?.image"/> -->

                <img :src="newsImage(currentNews?.images)"  style="max-height: 450px; width: 100%; object-fit: cover; border-radius: 20px;"  />

                <h4>{{ currentNews?.text }}</h4>
                <div class="flex-row">
                    <Button title="Предыдущая статья" @click="navigateToPrev" />
                    <Button title="Следующая статья" style="margin-left: auto;" @click="navigateToNext" />
                </div>
            </div>
            <div v-else style="margin-top: 40vh;">
                Новость не найдена, вернитесь на гравную страницу! {{ currentNews }}
            </div>
            <div class="flex-col desktop-only" style="gap: 20px; flex: 1; margin-left: 20px;" >
                <h2>Другие статьи</h2>
                <NewMiniCard v-for="news in  getLastFourItems()"
                    :title="news.title"
                    :icon="newsImage(news.images)"
                    :created_at="news.created_at.split('T')[0]"
                />
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, watch, computed } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import Button from '@/components/Button.vue';
import DateIcon from '@/assets/dateIcon.svg'
import NewMiniCard from '@/components/NewMiniCard.vue';

const route = useRoute();
const router = useRouter();
let newsId = parseInt(route.params.id, 10);
const currentNews = ref(null);

const newsData = JSON.parse(localStorage.getItem('news'));

const loadPage = () => {
    if (!newsData) return;
    currentNews.value = newsData.find(news => news.id == newsId);
    if (!currentNews.value) {}
}

onMounted(() => {
    loadPage()
});
watch(() => route.params.id, (newId) => {
    newsId = newId
    loadPage()
});

const getNewsFromLocalStorage = () => {
  return JSON.parse(localStorage.getItem('news') || '[]');
};

function getLastFourItems() {
  let arr = getNewsFromLocalStorage()
  arr = arr.filter(item => item.id !== parseInt(route.params.id, 10));
  if (arr.length < 4) {
    return arr;
  }
  return arr.slice(-4);
}

const navigateToOffset = (offset) => {
  const news = getNewsFromLocalStorage();
  const currentId = parseInt(route.params.id, 10);
  const currentIndex = news.findIndex(item => item.id === currentId);
  const newIndex = currentIndex + offset;

  if (newIndex >= 0 && newIndex < news.length) {
    const newItem = news[newIndex];
    router.push({ name: 'new', params: { id: newItem.id } });
  }
  return false
};

const navigateToPrev = () => {
  navigateToOffset(-1);
};

const navigateToNext = () => {
  navigateToOffset(1);
};

const newsImage = (images) => {
  return images.length > 0 ? `https://zayac.tech${images[0].url}` : '';
};
</script>