<template>
    <div id="news" class="flex-row justy-center alitems-center top-bottom-large-padding">
        <div class="flex-col alitems-center container-width large-gap">
            <div class="flex-col" style="gap: 12px; margin-right: auto;">
                <h1 class="text-align-mobile">Новости</h1>
            </div>
            <div class="flex-col medium-gap">
                <div
                    v-for="(chunk, index) in chunkedNews"
                    :key="index" class="mobile-wrap-column medium-gap"
                    style="word-wrap: break-word;"
                >
                      <NewsCard
                      v-for="news in chunk"
                      :key="news.id"
                      :title="news.title"
                      :body="news.body"
                      :icon="newsImage(news.images)"
                      style="flex: 1;"
                      @click="toNew(news.id)"

                      />
                </div>
            </div>
              <div v-if="cropped">
                <RouterLink to="/news">
                  <Button title="Все статьи" />
                </RouterLink>
              </div>
              <div v-else class="flex-row align-center justy-center" style="gap: 50%;">
                <Button title="Назад" @click="prevPage" :style="page == 0 ? { 'backgroundColor':  'grey' } : {}" style="margin-right: auto;" />
                <Button title="Вперед" @click="nextPage" :style="newsItems.length < (page + 1) * 12 ? { 'backgroundColor':  'grey' } : {}" style="margin-left: auto;" />
              </div>
        </div>
    </div>
</template>
<script setup>
import NewsCard from '@/components/NewsCard.vue';
import NewsFish from '@/assets/newsFish.png'
import Button from '@/components/Button.vue';
import { useRouter } from 'vue-router';
import { ref, onMounted, computed } from 'vue';

const props = defineProps({
  cropped: {
    type: Boolean,
    default: true
  }
})

const router = useRouter();
const newsItems = ref([]);
const page = ref(0)


const nextPage = () => {
  if (newsItems.value.length < (page.value + 1) * 12) return;
  page.value++
};

const prevPage = () => {
  if (page.value == 0) return;
  page.value--

};

function toNew(id) {
  router.push(`/new/${id}`);
}

function sortById(records) {
  return records.sort((a, b) => a.id - b.id);
}

const fetchNews = async () => {
  try {
    const response = await fetch('https://zayac.tech/ibgapi/news');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = sortById(await response.json());
    // const data = fakeNewsData
    localStorage.setItem('news', JSON.stringify(data))
    newsItems.value = data.map(newsItem => ({
      id: newsItem.id,
      title: newsItem.title,
      body: newsItem.text,
      created_at: newsItem.created_at,
      images: newsItem.images || []
    }));
  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
  }
};

const chunkArray = (array, chunkSize) => {
  if (props.cropped) {
    array = array.slice(-6);
  } else {
    // if (newsItems.value.length < page.value * 12) return;
    array = array.slice(page.value * 12, (page.value + 1) * 12)
  }


  const results = [];
  for (let i = 0; i < array.length; i += chunkSize) {
    results.push(array.slice(i, i + chunkSize));
  }
  return results;
};

const chunkedNews = computed(() => chunkArray(newsItems.value, 3));

const newsImage = (images) => {
  return images.length > 0 ? `https://zayac.tech${images[0].url}` : '';
};

onMounted(() => {
  fetchNews();
});


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














<!-- const fakeNewsData = [
  {
    id: 1,
    title: 'Ведение бухучёта',
    body: 'Первичка, учёт доходов и расходов, закрытие периода, отчётность по стандартам вашей юрисдикции.',
    images: [{ url: NewsFish }]
  },
  {
    id: 2,
    title: 'Расчётность',
    created_at: '23.23.2023',
    body: 'Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.',
    images: [{ url: NewsFish }]
  },
  {
    id: 3,
    title: 'Зарплата и кадры',
    body: 'Расчёт заработной платы, отпусков, больничных; кадровое делопроизводство и отчётность.',
    images: [{ url: NewsFish }]
  },
  {
    id: 4,
    title: 'Внутренний аудит',
    body: 'Проверка данных и процессов, рекомендации по снижению рисков, подготовка к внешнему аудиту.',
    images: [{ url: NewsFish }]
  },
  {
    id: 5,
    title: 'Консалтинг и учёт',
    body: 'Диагностика, регламенты, переход на аутсорс, построение учётной политики и контрольные процедуры.',
    images: [{ url: NewsFish }]
  },
  {
    id: 6,
    title: 'Автоматизация',
    body: 'Внедрение и поддержка 1С, интеграции с CRM/банками, сквозная аналитика.',
    images: [{ url: NewsFish }]
  },
    {
    id: 7,
    title: '2Консалтинг и учёт',
    body: 'Диагностика, регламенты, переход на аутсорс, построение учётной политики и контрольные процедуры.',
    images: [{ url: NewsFish }]
  },
  {
    id: 8,
    title: '2Автоматизация',
    body: 'Внедрение и поддержка 1С, интеграции с CRM/банками, сквозная аналитика.',
    images: [{ url: NewsFish }]
  },
    {
    id: 9,
    title: 'Ведение бухучёта',
    body: 'Первичка, учёт доходов и расходов, закрытие периода, отчётность по стандартам вашей юрисдикции.',
    images: [{ url: NewsFish }]
  },
  {
    id: 10,
    title: 'Расчётность',
    created_at: '23.23.2023',
    body: 'Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок.',
    images: [{ url: NewsFish }]
  },
  {
    id: 11,
    title: 'Зарплата и кадры',
    body: 'Расчёт заработной платы, отпусков, больничных; кадровое делопроизводство и отчётность.',
    images: [{ url: NewsFish }]
  },
  {
    id: 12,
    title: 'Внутренний аудит',
    body: 'Проверка данных и процессов, рекомендации по снижению рисков, подготовка к внешнему аудиту.',
    images: [{ url: NewsFish }]
  },
  {
    id: 13,
    title: 'Консалтинг и учёт',
    body: 'Диагностика, регламенты, переход на аутсорс, построение учётной политики и контрольные процедуры.',
    images: [{ url: NewsFish }]
  },
  {
    id: 14,
    title: 'Автоматизация',
    body: 'Внедрение и поддержка 1С, интеграции с CRM/банками, сквозная аналитика.',
    images: [{ url: NewsFish }]
  },
    {
    id: 15,
    title: '2Консалтинг и учёт',
    body: 'Диагностика, регламенты, переход на аутсорс, построение учётной политики и контрольные процедуры.',
    images: [{ url: NewsFish }]
  },
  {
    id: 16,
    title: '2Автоматизация',
    body: 'Внедрение и поддержка 1С, интеграции с CRM/банками, сквозная аналитика.',
    images: [{ url: NewsFish }]
  }
]; -->

<!-- <template>
    <div class="flex-row justy-center alitems-center top-bottom-large-padding">
        <div class="flex-col alitems-center container-width large-gap">
            <div class="flex-col" style="gap: 12px; margin-right: auto;">
                <img class="crown-text-margin" :src="BaseNewss" style="height: calc(6px + 3vh);" />
                <h1 class="text-align-mobile">Бухгалтерия, которой можно доверять</h1>
            </div>
            <div class="flex-col medium-gap">
                <div class="mobile-wrap-column medium-gap" style="word-wrap: break-word;">
                    <NewsCard style="flex: 1;" title="Ведение бухучёта" body="Первичка, учёт доходов и расходов, закрытие периода, отчётность по стандартам вашей юрисдикции." :icon="NewsFish"></NewsCard>
                    <NewsCard style="flex: 1;" title="Расчётность" body="Расчёт налогов, подача деклараций, сверки с ИФНС, сопровождение камеральных проверок." :icon="NewsFish"></NewsCard>
                    <NewsCard style="flex: 1;" title="Зарплата и кадры" body="Расчёт заработной платы, отпусков, больничных; кадровое делопроизводство и отчётность." :icon="NewsFish"></NewsCard>
                    </div>
                <div class="mobile-wrap-column medium-gap" style="word-wrap: break-word;">
                    <NewsCard style="flex: 1;" title="Внутренний аудит" body="Проверка данных и процессов, рекомендации по снижению рисков, подготовка к внешнему аудиту." :icon="NewsFish"></NewsCard>
                    <NewsCard style="flex: 1;" title="Консалтинг и учёт" body="Диагностика, регламенты, переход на аутсорс, построение учётной политики и контрольные процедуры." :icon="NewsFish"></NewsCard>
                    <NewsCard style="flex: 1;" title="Автоматизация" body="Внедрение и поддержка 1С, интеграции с CRM/банками, сквозная аналитика." :icon="NewsFish"></NewsCard>
                </div>
            </div>
            <Button title="Все статьи" />
        </div>
    </div>
</template>
<script setup>
import NewsCard from '@/components/NewsCard.vue';
import NewsFish from '@/assets/newsFish.png'
import Button from '@/components/Button.vue';

fetch()
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
</style> -->