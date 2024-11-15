from io import BytesIO
from PIL import ImageFont, Image
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from databases.models import Hosting_Website, Domains
from .base import DrawingTemplate, Coordinates2D


class PaymentSystemDrawingTemplate(DrawingTemplate):

    def __init__(self, background_image_path: str, session: AsyncSession):
        super().__init__(background_image_path)
        self.session = session

    async def _load_autocomplete_values(self):
        result = await self.session.execute(
            select(Domains.domain)
            .join(Hosting_Website, Domains.id == Hosting_Website.main_domain_id)
            .where(Hosting_Website.name.in_(["Payment", "Оплата"]))
        )

        domain_name = result.scalar_one_or_none()
        print("Domain: ", domain_name)
        if domain_name is None:
            raise ValueError("Domain not found")
        self.website_domain = domain_name

    def _init_fonts(self):
        self._font_iphone_time = ImageFont.truetype('assets/fonts/iphone_time.ttf')
        self._font_cario_semibold = ImageFont.truetype('assets/fonts/Cairo-SemiBold.ttf')

    def _init_assets(self):
        super()._init_assets()
        self._lock_icon = Image.open('assets/img/icons/lock.png')


class PaymentSystemNoteTemplate(PaymentSystemDrawingTemplate):
    class TextCoordinates:
        time = (80, 30)
        website_domain = Coordinates2D(lambda ws_domain: 560 - (len(ws_domain) - 1) * 10, 2178)

    def __init__(self, time: str, session: AsyncSession):
        super().__init__('assets/img/payment_sys/note.png', session)
        self.time = time
        self.website_domain = None

    # def _init_fonts(self):
    #     self._font_iphone_time = ImageFont.truetype('assets/fonts/iphone_time.ttf')
    #     self._font_cario_semibold = ImageFont.truetype('assets/fonts/Cairo-SemiBold.ttf')
    #
    # def _init_assets(self):
    #     super()._init_assets()
    #     self._lock_icon = Image.open('assets/img/icons/lock.png')

    def _generate(self) -> BytesIO:
        self._drawer.text(self.TextCoordinates.time, self.time, font=self._font_iphone_time.font_variant(size=45),
                          fill='#000000')
        ws_domain_x_coord = self.TextCoordinates.website_domain.x(self.website_domain)
        self._drawer.text(
            (ws_domain_x_coord, self.TextCoordinates.website_domain.y),
            self.website_domain,
            font=self._font_cario_semibold.font_variant(size=52),
            fill='#E5E5E5'
        )

        buffer = BytesIO()
        self._image.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer


class PaymentSystemRefundSuccessTemplate(PaymentSystemDrawingTemplate):
    class TextCoordinates:
        time = (80, 30)
        website_domain = Coordinates2D(lambda ws_domain: 540 - (len(ws_domain) - 1) * 10, 2174)

    def __init__(self, time: str, session: AsyncSession):
        super().__init__('assets/img/payment_sys/refund_success.png', session)
        self.time = time
        self.website_domain = None

    def _init_fonts(self):
        self._font_iphone_time = ImageFont.truetype('assets/fonts/iphone_time.ttf')
        self._font_cario_semibold = ImageFont.truetype('assets/fonts/Cairo-SemiBold.ttf')

    def _init_assets(self):
        super()._init_assets()
        self._lock_icon = Image.open('assets/img/icons/lock.png')

    def _generate(self) -> BytesIO:
        # Продолжаем с генерацией изображения
        self._drawer.text(self.TextCoordinates.time, self.time, font=self._font_iphone_time.font_variant(size=45),
                          fill='#000000')
        ws_domain_x_coord = self.TextCoordinates.website_domain.x(self.website_domain)
        self._drawer.text(
            (ws_domain_x_coord, self.TextCoordinates.website_domain.y),
            self.website_domain,
            font=self._font_cario_semibold.font_variant(size=52),
            fill='#E5E5E5'
        )

        buffer = BytesIO()
        self._image.save(buffer, format='PNG')
        buffer.seek(0)
        print(buffer)
        return buffer


class PaymentSystemNonEquivalently(PaymentSystemDrawingTemplate):
    class TextCoordinates:
        time = (80, 30)
        website_domain = Coordinates2D(lambda ws_domain: 540 - (len(ws_domain) - 1) * 10, 2174)

    def __init__(self, time: str, session: AsyncSession):
        super().__init__('assets/img/payment_sys/not_equivalently.png', session)
        self.time = time
        self.website_domain = None

    def _generate(self) -> BytesIO:
        self._drawer.text(self.TextCoordinates.time, self.time, font=self._font_iphone_time.font_variant(size=45),
                          fill='#000000')
        ws_domain_x_coord = self.TextCoordinates.website_domain.x(self.website_domain)
        self._drawer.text(
            (ws_domain_x_coord, self.TextCoordinates.website_domain.y),
            self.website_domain,
            font=self._font_cario_semibold.font_variant(size=52),
            fill='#E5E5E5'
        )

        buffer = BytesIO()
        self._image.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer


class PaymentSystemTransactionRestricted(PaymentSystemDrawingTemplate):
    class TextCoordinates:
        time = (80, 30)
        website_domain = Coordinates2D(lambda ws_domain: 540 - (len(ws_domain) - 1) * 10, 2174)

    def __init__(self, time: str, session: AsyncSession):
        super().__init__('assets/img/payment_sys/transaction_restricted.png', session)
        self.time = time
        self.website_domain = None

    def _generate(self) -> BytesIO:
        self._drawer.text(self.TextCoordinates.time, self.time, font=self._font_iphone_time.font_variant(size=45),
                          fill='#000000')
        ws_domain_x_coord = self.TextCoordinates.website_domain.x(self.website_domain)
        self._drawer.text(
            (ws_domain_x_coord, self.TextCoordinates.website_domain.y),
            self.website_domain,
            font=self._font_cario_semibold.font_variant(size=52),
            fill='#E5E5E5'
        )

        buffer = BytesIO()
        self._image.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer


class PaymentSystemUnknownError(PaymentSystemDrawingTemplate):
    class TextCoordinates:
        time = (80, 30)
        website_domain = Coordinates2D(lambda ws_domain: 540 - (len(ws_domain) - 1) * 10, 2174)

    def __init__(self, time: str, session: AsyncSession):
        super().__init__('assets/img/payment_sys/unknown_error.png', session)
        self.time = time
        self.website_domain = None

    def _generate(self) -> BytesIO:
        self._drawer.text(self.TextCoordinates.time, self.time, font=self._font_iphone_time.font_variant(size=45),
                          fill='#000000')
        ws_domain_x_coord = self.TextCoordinates.website_domain.x(self.website_domain)
        self._drawer.text(
            (ws_domain_x_coord, self.TextCoordinates.website_domain.y),
            self.website_domain,
            font=self._font_cario_semibold.font_variant(size=52),
            fill='#E5E5E5'
        )

        buffer = BytesIO()
        self._image.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer


class PaymentSystemCardNotSupported(PaymentSystemDrawingTemplate):
    class TextCoordinates:
        time = (80, 30)
        website_domain = Coordinates2D(lambda ws_domain: 540 - (len(ws_domain) - 1) * 10, 2174)

    def __init__(self, time: str, session: AsyncSession):
        super().__init__('assets/img/payment_sys/card_not_supported.png', session)
        self.time = time
        self.website_domain = None

    def _generate(self) -> BytesIO:
        self._drawer.text(self.TextCoordinates.time, self.time, font=self._font_iphone_time.font_variant(size=45),
                          fill='#000000')
        ws_domain_x_coord = self.TextCoordinates.website_domain.x(self.website_domain)
        self._drawer.text(
            (ws_domain_x_coord, self.TextCoordinates.website_domain.y),
            self.website_domain,
            font=self._font_cario_semibold.font_variant(size=52),
            fill='#E5E5E5'
        )

        buffer = BytesIO()
        self._image.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer


class PaymentSystemIncorrectOrderNumber(PaymentSystemDrawingTemplate):
    class TextCoordinates:
        time = (80, 30)
        website_domain = Coordinates2D(lambda ws_domain: 560 - (len(ws_domain) - 1) * 10, 2178)

    def __init__(self, time: str, session: AsyncSession):
        super().__init__('assets/img/payment_sys/incorrect_order_number.png', session)
        self.time = time
        self.website_domain = None

    def _generate(self) -> BytesIO:
        self._drawer.text(self.TextCoordinates.time, self.time, font=self._font_iphone_time.font_variant(size=45),
                          fill='#000000')
        ws_domain_x_coord = self.TextCoordinates.website_domain.x(self.website_domain)
        self._drawer.text(
            (ws_domain_x_coord, self.TextCoordinates.website_domain.y),
            self.website_domain,
            font=self._font_cario_semibold.font_variant(size=52),
            fill='#E5E5E5'
        )

        buffer = BytesIO()
        self._image.save(buffer, format='PNG')
        buffer.seek(0)

        return buffer
