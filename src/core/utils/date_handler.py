from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo  # built in|out of the box| suportar fusos específicos (como America/Sao_Paulo)


class DateHandler:
    """Classe utilitária para manipulação de datas e horas com timezone."""

    @staticmethod
    def now_utc() -> datetime:
        """Retorna o horário atual em UTC (com timezone)."""
        return datetime.now(timezone.utc)

    @staticmethod
    def now_local(tz_name: str = "America/Sao_Paulo") -> datetime:
        """Retorna o horário atual em um timezone específico."""
        tz = pytz.timezone(tz_name)
        return datetime.now(tz)

    @staticmethod
    def to_local(dt: datetime, tz_name: str = "America/Sao_Paulo") -> datetime:
        """Converte um datetime UTC para o horário local."""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        tz = pytz.timezone(tz_name)
        return dt.astimezone(tz)

    @staticmethod
    def to_utc(dt: datetime) -> datetime:
        """Converte qualquer datetime para UTC (aware)."""
        if dt.tzinfo is None:
            raise ValueError("Datetime deve conter fuso horário para conversão segura.")
        return dt.astimezone(timezone.utc)

    @staticmethod
    def add_minutes(minutes: int) -> datetime:
        """Retorna um datetime UTC com X minutos a mais (para tokens, etc)."""
        return DateHandler.now_utc() + timedelta(minutes=minutes)

    @staticmethod
    def add_days(days: int) -> datetime:
        """Retorna um datetime UTC com X dias a mais."""
        return DateHandler.now_utc() + timedelta(days=days)

    @staticmethod
    def format_iso(dt: datetime) -> str:
        """Formata um datetime UTC em ISO 8601."""
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.isoformat()


date_handler = DateHandler()
