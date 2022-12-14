from django.contrib import admin
from blog.models import *

# Register your models here.


admin.site.register(Index_First_Slider)


MAX_OBJECTS = 1


@admin.register(Index_Settings)
class AdminIndexSettings(admin.ModelAdmin):

    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


admin.site.register(Services)
admin.site.register(Service_Images)


admin.site.register(Options)


class OptionInline(admin.StackedInline):
    model = Options
    max_num = 5
    extra = 1


@admin.register(Offers)
class AdminOffers(admin.ModelAdmin):
    inlines = [OptionInline,]


@admin.register(Booking)
class AdminBooking(admin.ModelAdmin):
    list_display = ['email','number','book_date']



############################################
admin.site.register(Why_Options)


class OptionWhyInline(admin.StackedInline):
    model = Why_Options
    max_num = 8
    extra = 1


@admin.register(Why_Us_Detail)
class AdminOffers(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    inlines = [OptionWhyInline,]


# admin.site.register(Work)
# admin.site.register(Images)
admin.site.register(Category)


class ImageInline(admin.StackedInline):
    model = Images
    max_num = 50
    extra = 1


@admin.register(Work)
class AdminWork(admin.ModelAdmin):
    inlines = [ImageInline,]


admin.site.register(AboutSliderImage)


class ImageSlider(admin.StackedInline):
    model = AboutSliderImage
    max_num = 5
    extra = 1


@admin.register(About)
class AdminOffers(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)
    inlines = [ImageSlider,]

admin.site.register(Member)


@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= MAX_OBJECTS:
            return False
        return super().has_add_permission(request)


admin.site.register(Message)


admin.site.register(GeneralSettings)
