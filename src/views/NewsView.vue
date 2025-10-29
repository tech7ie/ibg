<script setup>
import NewsSection from '@/sections/NewsSection.vue';
</script>

<template>
    <div  class="flex-col alitems-center" style="width: 100%; margin-top: 40px; margin-bottom: 40px;">
		<section>
			<NewsSection :cropped="false" />
		</section>
    </div>
</template>
