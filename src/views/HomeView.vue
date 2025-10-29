<script setup>
import MainSection from '@/sections/MainSection.vue';
import WhyWeSection from '@/sections/WhyWeSection.vue';
import StorySection from '@/sections/StorySection.vue';
import YouGetSecrion from '@/sections/YouGetSecrion.vue';
import ServicesSection from '@/sections/ServicesSection.vue';
import CompaniesSection from '@/sections/CompaniesSection.vue';
import NewsSection from '@/sections/NewsSection.vue';
</script>

<template>
    <main>
		<section>
			<MainSection />
		</section>
		<section>
			<WhyWeSection />
		</section>
		<section>
			<StorySection />
		</section>
		<section>
			<YouGetSecrion />
		</section>
		<section>
			<NewsSection />
		</section>
		<section>
			<ServicesSection />
		</section>
		<section>
			<CompaniesSection />
		</section>
    </main>
</template>
