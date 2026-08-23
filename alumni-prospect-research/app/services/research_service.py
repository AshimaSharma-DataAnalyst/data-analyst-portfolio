from app.services.company_service import CompanyService
from app.services.llm_service import LLMService
from app.services.prompt_service import PromptService
from app.utils.logger import logger


class ResearchService:
    """
    Builds a complete alumni research profile.

    Steps:
    1. Get company information.
    2. Build AI prompt.
    3. Generate AI summary.
    4. Return complete profile.
    """

    def __init__(self):

        self.company_service = CompanyService()

        self.prompt_service = PromptService()

        self.llm = LLMService()

        logger.info("Research Service initialized.")

    def build_profile(self, alumni):

        logger.info(
            f"Building research profile for {alumni.get('name', 'Unknown')}"
        )

        try:

            company = alumni.get("company", "")

            logger.info(f"Fetching company information for {company}")

            company_info = self.company_service.get_company_information(
                company
            )

            profile = {

                "name": alumni.get("name", ""),

                "company": company,

                "designation": alumni.get("designation", ""),

                "education": alumni.get("education", ""),

                "city": alumni.get("city", ""),

                "industry": company_info.get("industry", ""),

                "company_type": company_info.get("company_type", ""),

                "headquarters": company_info.get("headquarters", ""),

                "website": company_info.get("website", "")

            }

            logger.info("Building AI prompt...")

            prompt = self.prompt_service.build_prompt(profile)

            logger.info("Generating AI summary...")

            ai_summary = self.llm.generate(prompt)

            profile["summary"] = ai_summary

            logger.success(
                f"Research profile created for {profile['name']}"
            )

            return profile

        except Exception as e:

            logger.exception(
                f"Failed to build profile for {alumni.get('name', 'Unknown')}"
            )

            raise