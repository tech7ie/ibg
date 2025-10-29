<template>
    <div class="flex-row justy-center alitems-center  large-gap top-bottom-large-padding" >
        <div class="flex-col alitems-center container-width  large-gap">
            <h1 style="margin-right: auto;" class="text-align-mobile">С нами работают компании из разных отраслей</h1>
            <div ref="scrollContainer" style="overflow: auto; width: 100%;" class="flex-row off-scroll medium-gap">
                <CompanyCard :img="ComVisa"/>
                <CompanyCard :img="ComVisa"/>
                <CompanyCard :img="ComVisa"/>
                <CompanyCard :img="ComVisa"/>
            </div>
        </div>
    </div>
</template>
<script setup>
import CompanyCard from '@/components/CompanyCard.vue'
import ComVisa from '@/assets/comVisa.svg'
import { ref, onMounted } from 'vue';

const scrollContainer = ref(null);
const scrollSpeed = 1.2;
let direction = 'right';

const startScrolling = () => {
  const scroll = () => {
    if (!scrollContainer.value) return;

    const container = scrollContainer.value;
    
    if (direction === 'right') {
      if (container.scrollLeft + container.clientWidth < container.scrollWidth-10) {
        container.scrollLeft += scrollSpeed;
      } else {
        direction = 'left';
      }
    } else if (direction === 'left') {
      if (container.scrollLeft > 10) {
        container.scrollLeft -= scrollSpeed;
      } else {
        direction = 'right';
      }
    }
    
    requestAnimationFrame(scroll);
  };

  scroll();
};

onMounted(() => {
  startScrolling();
});
</script>